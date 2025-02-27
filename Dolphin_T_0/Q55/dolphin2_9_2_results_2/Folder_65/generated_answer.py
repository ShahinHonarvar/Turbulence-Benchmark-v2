from itertools import combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for r in range(1, n + 1):
        for c in combinations(lst, r):
            if c[0] != 1 and c[-1] != 1 and (np.prod(c) == 46):
                sublists.append(c)
    return sublists