from collections import deque
import numpy as np

def lists_with_product_equal_n(lst):
    circular_lst = deque(lst)
    circular_lst.extend(lst[:-1])
    result = []
    for i in range(len(circular_lst) - len(lst) + 1):
        for j in range(i + 1, i + len(lst) + 1):
            sublist = list(circular_lst)[i:j]
            if np.prod(sublist) == 990:
                result.append(sublist)
    return result