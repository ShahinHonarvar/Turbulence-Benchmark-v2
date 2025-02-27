import itertools

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def lists_with_product_equal_n(lst):
    lst = lst + lst[0:1]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if product(lst[i:j]) == 48:
                return lists_with_product_equal_n.sublists + [lst[i:j]]
    return lists_with_product_equal_n.sublists