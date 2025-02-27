from itertools import combinations
from math import prod

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for j in range(len(lst)):
            for sublist in combinations(lst[j:] + lst[:j], i):
                if prod(sublist) == -95:
                    result.append(list(sublist))
    return result