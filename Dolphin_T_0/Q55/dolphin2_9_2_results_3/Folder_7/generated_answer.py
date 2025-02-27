from itertools import combinations, permutations
import operator
from functools import reduce

def list_with_product_equal_n(lst):
    sublists = []
    for r in range(len(lst) + 1):
        for comb in combinations(lst, r):
            if reduce(operator.mul, comb, 1) == 537:
                sublists.append(comb)
    return sublists if sublists else []

def lists_with_product_equal_n(lst):
    result = []
    lst = list(lst)
    n = len(lst)
    for i in range(n):
        for sublist in list_with_product_equal_n(lst):
            result.append(sublist)
        lst = lst[1:] + [lst[0]]
    return result