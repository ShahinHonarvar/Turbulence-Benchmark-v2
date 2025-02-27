from itertools import product

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:]
    sublists = [lst[i:j] for i in range(n) for j in range(i + 1, n + 1)]
    result = [sublist for sublist in sublists if sublist.product() == 76]
    return result