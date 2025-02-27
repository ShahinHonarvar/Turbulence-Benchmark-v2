from itertools import islice, cycle
from more_itertools import windowed

def lists_with_product_equal_n(lst):
    n = -93
    result = []
    for i in range(1, len(lst) + 1):
        for sublst in windowed(lst, i):
            if is_contiguous(sublst) and product(sublst) == n:
                result.append(list(sublst))
    return result

def is_contiguous(lst):
    return len(lst) == len(set(lst))

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)