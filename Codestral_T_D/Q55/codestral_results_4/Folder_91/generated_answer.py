from collections import deque
from itertools import combinations

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = 2
    result = []
    for r in range(1, len(lst) + 1):
        for _ in range(len(lst)):
            sublist = list(lst)
            if sublist[:r] not in result and prod(sublist[:r]) == n:
                result.append(sublist[:r])
            lst.rotate(-1)
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p