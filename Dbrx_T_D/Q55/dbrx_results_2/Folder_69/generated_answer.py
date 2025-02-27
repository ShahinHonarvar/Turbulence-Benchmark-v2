from itertools import islice

def circular_sublists(lst):
    return [lst[i:] + lst[:i] for i in range(len(lst))]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def find_sublists_with_product(lst, n):
    return [sublist for sublist in circular_sublists(lst) if product(sublist) == n]

def lists_with_product_equal_n(lst, n):
    return [sublist for sublist in [find_sublists_with_product(lst[i:j], n) for i in range(len(lst)) for j in range(i, len(lst) + 1)] if sublist]