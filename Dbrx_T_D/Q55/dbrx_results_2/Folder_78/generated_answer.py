from itertools import islice

def circular_slice(lst, start, end):
    return lst[start:end] + lst[:end - len(lst)] if end > len(lst) else lst[start:end]

def circular_sublists(lst):
    return [circular_slice(lst, i, i + j) for i in range(len(lst)) for j in range(1, len(lst) - i + 1)]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n=74):
    return [sublst for sublst in circular_sublists(lst) if product(sublst) == n]