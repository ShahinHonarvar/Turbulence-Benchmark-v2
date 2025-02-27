from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -10
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if reduce(lambda x, y: x * y, sublist) == n:
            result.append(sublist)
    return result