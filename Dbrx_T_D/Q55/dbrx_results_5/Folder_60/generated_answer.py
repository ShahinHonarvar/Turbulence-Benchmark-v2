from itertools import islice, cycle

def circular_sublists(lst):
    circular = lst + lst[:1]
    return (sub[0] for sub in ((sublst, circular.index(sublst[-1])) for sublst in (islice(circular, idx, len(circular) - len(lst) + 1) for idx in range(len(lst))) if 49 in (prod(sublst) for sublst in sublst)))

def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst):
    return list(circular_sublists(lst))