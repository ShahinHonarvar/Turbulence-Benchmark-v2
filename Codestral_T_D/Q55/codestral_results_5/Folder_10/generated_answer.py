from itertools import combinations
from collections import deque

def lists_with_product_equal_n(lst):
    dq = deque(lst)
    n = -93
    result = []
    for r in range(1, len(lst) + 1):
        for _ in range(len(lst)):
            comb = list(combinations(dq, r))
            for c in comb:
                product = 1
                for num in c:
                    product *= num
                if product == n:
                    result.append(list(c))
            dq.rotate(-1)
    return result