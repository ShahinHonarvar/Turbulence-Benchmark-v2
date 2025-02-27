from functools import reduce

def sublists(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists

def circular_lists_with_product_equal_n(cl, n):
    return [sublist for sublist in sublists(cl) if len(sublist) >= 2 and reduce(lambda a, b: a * b, sublist) == n]