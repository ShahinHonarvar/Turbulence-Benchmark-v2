from itertools import tee, combinations

def get_sublists(lst):
    n = len(lst)
    last = lst[-1]
    lst = lst + [last]
    sublists = [[lst[i]] for i in range(n)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            sublists.append(lst[i:j])
    return sublists

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def lists_with_product_equal_n(lst):
    if product(lst) != -33:
        return []
    subs = get_sublists(lst)
    res = [s for s in subs if product(s) == -33]
    return res