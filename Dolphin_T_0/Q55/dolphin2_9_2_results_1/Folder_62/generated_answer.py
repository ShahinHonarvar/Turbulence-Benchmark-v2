from itertools import combinations
from math import prod
from functools import reduce

def lists_with_product_equal_n(lst):
    length = len(lst)
    combinations_list = [lst[i:j] for i in range(length) for j in range(i + 1, length + 1)]
    return [list_val for list_val in combinations_list if prod(list_val) == 100]