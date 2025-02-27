import math
from itertools import islice, cycle

def cycle_iterator(iterable):
    return cycle(islice(iterable, len(iterable) * 2))

def product(lst):
    result = 1
    for number in lst:
        result *= number
    return result

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for length in range(1, len(lst) + 1):
            sublist = [lst[i]] + list(islice(cycle_iterator(lst), 1, length))
            if product(sublist) == 47:
                result.append(sublist)
    return result