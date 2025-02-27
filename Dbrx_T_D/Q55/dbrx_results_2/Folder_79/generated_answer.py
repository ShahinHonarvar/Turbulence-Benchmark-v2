from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(1, len(lst) + 1):
        for sublst in combinations(lst, i):
            if list(islice(cycle(sublst), len(lst) - 1))[0] * sublst[-1] == -83:
                sublists.append(list(sublst))
    return sublists