from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    lst = list(lst)
    lst_cycle = cycle(lst)
    size = len(lst)
    product = 1
    for i in range(size):
        product *= lst[i]
    if product != 46:
        return []
    sublist_set = set()
    for i in range(size):
        sublist = []
        for j in range(size):
            sublist.append(next(lst_cycle))
            product = 1
            for k in sublist:
                product *= k
            if product == 46:
                sublist_set.add(tuple(sublist))
    sublists = []
    for sublist in sublist_set:
        sublists.append(list(sublist))
    return sublists