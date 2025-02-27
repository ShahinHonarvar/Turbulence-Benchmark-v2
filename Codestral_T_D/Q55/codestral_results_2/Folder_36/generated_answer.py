from collections import deque
import numpy as np

def lists_with_product_equal_n(lst):
    n = 714
    lst = deque(lst)
    res = []
    for _ in range(len(lst)):
        lst.rotate(-1)
        prefix_product = np.cumprod([1] + list(lst))
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                if prefix_product[j] // prefix_product[i] == n:
                    res.append(list(lst)[i:j])
    return res