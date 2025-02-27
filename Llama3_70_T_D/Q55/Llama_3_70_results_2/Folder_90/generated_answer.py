from itertools import combinations
from math import prod

def lists_with_product_equal_n(lst):
    result = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            for combo in combinations(lst[i:] + lst[:i], r):
                if prod(combo) == -690:
                    result.append(list(combo))
    return result