from itertools import combinations
from functools import reduce
import operator

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(1, len(lst) + 1):
        circ = lst[-i:] + lst[:-i]
        for comb in combinations(circ, i):
            if reduce(operator.mul, comb, 1) == 46:
                sublists.append(comb)
    return sublists