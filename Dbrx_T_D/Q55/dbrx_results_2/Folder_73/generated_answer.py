from itertools import combinations

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(1, len(lst) + 1):
        for j in combinations(lst, i):
            if int(functools.reduce(lambda x, y: x * y, j)) == 40:
                sublists.append(list(j))
    return sublists