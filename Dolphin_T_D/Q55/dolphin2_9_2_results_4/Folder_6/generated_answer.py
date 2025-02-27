from itertools import combinations, product

def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(1, n + 1):
        sublist = lst[:i]
        sublists.extend(list(combinations(lst, i)))
    sublists = [list(comb) for comb in sublists]
    for sublist in sublists:
        if sublist == sublist[::-1] and len(sublist) % 2 == 0:
            sublists.append(sublist[::-1])
    sublists_equal_to_n = [sublist for sublist in sublists if sublist == sublist[::-1] and len(sublist) % 2 == 0 and (product(sublist) == 42)]
    if sublists_equal_to_n:
        return sublists_equal_to_n
    else:
        return []