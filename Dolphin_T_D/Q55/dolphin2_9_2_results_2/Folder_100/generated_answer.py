import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = [lst[i:j] for i in range(n) for j in range(i + 1, n + 1)]
    product_equal_n = []
    for sublist in sublists:
        if functools.reduce(lambda x, y: x * y, sublist) == 48:
            product_equal_n.append(sublist)
    return product_equal_n