from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 57
    circular_list = list(circular_list)
    result = []
    for i in range(len(circular_list)):
        sublists = [list(islice(circular_list, i, i + j)) for j in range(1, len(circular_list))]
        for sublist in sublists:
            if len(sublist) > 0 and all((num in circular_list for num in sublist)) and (n in [prod(sublist)]):
                result.append(sublist)
    return result