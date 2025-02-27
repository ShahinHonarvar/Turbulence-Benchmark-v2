from collections import deque
from functools import reduce
import operator

def lists_with_product_equal_n(circ_list):
    n = -10
    result = []
    for i in range(len(circ_list)):
        prod = 1
        for j in range(i, len(circ_list) + i):
            prod *= circ_list[j % len(circ_list)]
            if prod == n:
                result.append(circ_list[i:j % len(circ_list) + 1] if j % len(circ_list) >= i else circ_list[i:] + circ_list[:j % len(circ_list) + 1])
            if abs(prod) > abs(n):
                break
    return result