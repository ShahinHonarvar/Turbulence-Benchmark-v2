from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -97
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list[i:]), len(circular_list)))
        if prod(sublist) == n:
            result.append(sublist)
    return result

def prod(iterable):
    product = 1
    for i in iterable:
        product *= i
    return product