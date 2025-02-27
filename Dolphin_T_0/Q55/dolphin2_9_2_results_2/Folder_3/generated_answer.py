from itertools import combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 1:
        if lst[0] == -22 or lst[0] == 22:
            return [lst]
        else:
            return []
    sublists = []
    for i in range(2, n + 1):
        for c in combinations(lst, i):
            product = 1
            for x in c:
                product *= x
            if product == -22:
                sublists.append(list(c))
    return sublists