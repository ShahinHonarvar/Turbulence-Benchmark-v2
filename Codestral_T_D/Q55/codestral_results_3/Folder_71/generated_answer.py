from typing import List
import numpy as np

def lists_with_product_equal_n(lst: List[int]) -> List[List[int]]:
    n = 47
    result = []
    len_lst = len(lst)
    lst = lst + lst
    for i in range(len_lst):
        product = 1
        for j in range(i, i + len_lst):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product > n:
                break
    return result