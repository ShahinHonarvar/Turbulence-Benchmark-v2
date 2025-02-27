from functools import reduce
from operator import mul

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:-1]
    valid_sublists = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sub_list = lst[i:j]
            product = reduce(mul, sub_list, 1)
            if product == 36:
                valid_sublists.append(sub_list)
    return valid_sublists