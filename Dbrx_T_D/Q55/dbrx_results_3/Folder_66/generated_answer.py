from itertools import islice, cycle

def circular_list_slice(it, start, stop):
    sl = islice(it, start, stop)
    return [sl, tuple(islice(cycle(sl), stop - start))]

def prune_sublists(sublists):
    return [sl for sl in sublists if sl]

def sublists_with_product_equal_n(lst, n):
    if not lst:
        return []
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublists.append(circular_list_slice(lst, i, j + 1))
    pruned_sublists = prune_sublists(sublists)
    sublists_with_product_equal_n = [sl for sl in pruned_sublists if sublists_product(sl) == n]
    return sublists_with_product_equal_n

def sublists_product(sublists):
    return reduce(lambda x, y: x * y, [sublists]) if sublists else 1