from collections import deque
from itertools import combinations
import numpy as np

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = -36
    sublists = []
    for _ in range(len(lst)):
        for r in range(2, len(lst) + 1):
            for sublist in combinations(lst, r):
                if np.prod(sublist) == n:
                    sublists.append(list(sublist))
        lst.rotate(-1)
    return sublists