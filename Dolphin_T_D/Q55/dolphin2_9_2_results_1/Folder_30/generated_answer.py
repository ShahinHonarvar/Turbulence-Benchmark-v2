from itertools import combinations

def lists_with_product_equal_n(lst):
    lst = lst + lst[:1]
    sublists = []
    for r in range(2, len(lst) + 1):
        for c in combinations(lst, r):
            if 1 <= r <= len(lst) and c[0] * c[-1] == 99 and (c[-1] * c[0] == 99):
                sublists.append(c)
    return list(sublists)