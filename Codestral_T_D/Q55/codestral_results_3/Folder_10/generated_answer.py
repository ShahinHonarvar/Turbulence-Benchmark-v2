from itertools import product, combinations
from math import prod

def lists_with_product_equal_n(lst):
    sublists = []
    for r in range(1, len(lst) + 1):
        for subs in combinations(lst * 2, r):
            if prod(subs) == -93:
                sublists.append(list(subs))
    return sublists