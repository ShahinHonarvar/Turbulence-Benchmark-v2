from itertools import islice, chain
import numpy as np

def circular_list_product(lst, size):
    return [lst[i:i + size] for i in range(len(lst)) if i + size <= len(lst)]

def lists_with_product_equal_n(lst, n):
    return [sublist for sublist in circular_list_product(lst, len(lst)) if np.prod(sublist) == n]

def sublists_with_product_equal_n(lst, n):
    return [sublist for maxlen in range(1, len(lst) + 1) for sublist in sublists_with_maxlen(lst, maxlen) if np.prod(sublist) == n]

def sublists_with_maxlen(lst, maxlen):
    return (list(sublist) for i in range(maxlen) for sublist in islice(sublists(lst), i, None))

def sublists(lst):
    yield from (lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1))