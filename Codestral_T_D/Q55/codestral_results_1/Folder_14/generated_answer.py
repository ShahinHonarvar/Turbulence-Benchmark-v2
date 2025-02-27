from itertools import combinations
from functools import reduce
import operator

def lists_with_product_equal_n(lst):
    n = -72
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i):
            sublist = lst[i:j]
            product = reduce(operator.mul, sublist, 1)
            if product == n:
                result.append(sublist)
    return result