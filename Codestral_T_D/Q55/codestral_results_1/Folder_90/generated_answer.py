from itertools import combinations

def lists_with_product_equal_n(lst):
    extended_lst = lst + lst
    n = -690
    result = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            for sublist in combinations(extended_lst[i:i + len(lst)], r):
                if prod(sublist) == n:
                    result.append(list(sublist))
    return [list(x) for x in set((tuple(sorted(sub)) for sub in result))]