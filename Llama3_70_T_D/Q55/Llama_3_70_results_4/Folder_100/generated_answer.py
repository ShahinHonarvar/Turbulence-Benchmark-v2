from itertools import accumulate
from math import prod
from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    dq = deque(lst)
    result = set()
    for _ in range(n):
        for i in range(1, n + 1):
            temp = list(dq)[:i]
            if prod(temp) == 48:
                result.add(tuple(temp))
        dq.rotate(1)
    return [list(i) for i in result]