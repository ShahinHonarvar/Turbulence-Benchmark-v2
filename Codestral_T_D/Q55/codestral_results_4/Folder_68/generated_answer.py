from itertools import permutations

def lists_with_product_equal_n(lst):
    n = 6
    res = []
    for r in range(1, len(lst) + 1):
        for sub in permutations(lst * 2, r):
            if sub[-1] == sub[0]:
                sub = sub[:-1]
                if sub not in res and prod(sub) == n:
                    res.append(sub)
    return res

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p