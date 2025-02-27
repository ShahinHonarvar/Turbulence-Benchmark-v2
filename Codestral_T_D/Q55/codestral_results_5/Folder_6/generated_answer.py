from collections import deque
import numpy as np

def lists_with_product_equal_n(lst):
    circular_lst = deque(lst)
    n = len(lst)
    result = []
    for _ in range(n):
        for i in range(1, n):
            sublist = list(circular_lst)[:i]
            if np.prod(sublist) == 42:
                result.append(sublist)
        circular_lst.rotate(-1)
    return result