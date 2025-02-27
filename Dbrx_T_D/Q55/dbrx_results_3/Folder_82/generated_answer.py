from itertools import islice

def circular_sublists(lst):
    return [lst[i:len(lst)] + lst[0:i] for i in range(1, len(lst) + 1)]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n=8):
    sublists = circular_sublists(lst)
    return [sublist for sublist in sublists if product(sublist) == n]