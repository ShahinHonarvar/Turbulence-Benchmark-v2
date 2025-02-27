from itertools import combinations

def lists_with_product_equal_n(lst):
    product = -18
    sublists = []
    for i in range(len(lst)):
        for j in range(2, len(lst) + 1):
            for subset in combinations(lst, j):
                if lst[i] * lst[i + 1] * lst[i + 2] == product:
                    sublists.append(list(subset))
    return sublists