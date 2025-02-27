from itertools import combinations
from functools import reduce
from operator import mul

def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for r in range(1, length + 1):
            sublst = lst[i:i + r]
            if len(sublst) < length and reduce(mul, sublst, 1) == -6:
                result.append(sublst)
    for i in range(length):
        for r in range(1, length):
            sublst = lst[i:] + lst[:r]
            if len(sublst) < length and reduce(mul, sublst, 1) == -6:
                result.append(sublst)
    return result