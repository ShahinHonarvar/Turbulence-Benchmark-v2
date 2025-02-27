from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=32):
    sublists = []
    for i in range(len(lst)):
        sublist = list(islice(cycle(lst[i:]), len(lst)))
        if prod(sublist) == n:
            sublists.append(sublist)
    return sublists

def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1)