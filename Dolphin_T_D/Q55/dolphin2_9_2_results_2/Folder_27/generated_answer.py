from itertools import islice, starmap
from math import prod

def circular_permutations(lst):
    return [lst[i:] + lst[:i] for i in range(len(lst))]

def is_equal_to_n(sublist, n):
    return prod(sublist) == n

def lists_with_product_equal_n(lst, n=-82):
    circular_lst = circular_permutations(lst)
    sublists = [islice(circular_lst[i], j, j + len(lst)) for i in range(len(lst)) for j in range(len(lst))]
    equal_to_n = [sublist for sublist in sublists if is_equal_to_n(sublist, n)]
    return equal_to_n