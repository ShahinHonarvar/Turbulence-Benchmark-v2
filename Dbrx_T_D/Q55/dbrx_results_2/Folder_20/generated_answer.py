from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = -69
    sublists = []
    circular_lst = cycle(lst)
    for i in range(len(lst)):
        sublst = tuple(islice(circular_lst, i + 1))
        if sublst and product(sublst) == n:
            sublists.append(list(sublst))
        circular_lst = circular_lst[-1:] + circular_lst[:-1]
    return sublists

def product(lst):
    if not lst:
        return 1
    p = 1
    for i in lst:
        p *= i
    return p