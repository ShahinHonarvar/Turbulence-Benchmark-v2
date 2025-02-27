from itertools import islice

def circular_sublists(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i, len(lst) + 1)]

def products_equal_n(lst, n):
    circular_sublists_of_l = circular_sublists(lst)
    valid_sublists = [s for s in circular_sublists_of_l if reduce(lambda x, y: x * y, s, 1) == n]
    return valid_sublists

def lists_with_product_equal_n(lst):
    return products_equal_n(lst, -16)