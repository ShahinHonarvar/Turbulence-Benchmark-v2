from itertools import combinations
from collections import deque

def lists_with_product_equal_n(lst):
    circular_lst = deque(lst + lst)
    sublists = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = list(circular_lst)[i:i + r]
            product = 1
            for num in sublist:
                product *= num
            if product == -97:
                sublists.append(sublist)
    return sublists