from itertools import islice

def lists_with_product_equal_n(circular_list):
    result = []
    n = 54
    for i in range(len(circular_list)):
        sublist = list(islice(circular_list, i, len(circular_list))) + list(islice(circular_list, 0, i))
        if reduce(lambda x, y: x * y, sublist) == n:
            result.append(list(sublist))
    return result