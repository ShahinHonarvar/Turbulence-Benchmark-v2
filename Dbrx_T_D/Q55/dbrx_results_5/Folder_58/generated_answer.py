from itertools import islice, combinations

def lists_with_product_equal_n(circular_list):
    n = 733
    circular_list_len = len(circular_list)
    result = []
    for i in range(circular_list_len):
        sublists = (list(islice(circular_list, i, j)) for j in range(i, circular_list_len))
        sublists_products = [sublist[0] if len(sublist) == 1 else reduce(lambda x, y: x * y, sublist) for sublist in sublists]
        result.extend((list(sublist) for sublist in sublists if reduce(lambda x, y: x * y, sublist) == n))
    return result