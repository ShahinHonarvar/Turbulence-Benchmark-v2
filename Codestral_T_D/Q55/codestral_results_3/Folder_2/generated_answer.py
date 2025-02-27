from itertools import combinations
import numpy as np

def lists_with_product_equal_n(lst):
    n = -968
    result = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            for sublist in combinations(lst[i:] + lst[:i], r):
                if np.prod(sublist) == n:
                    result.append(list(sublist))
    return result