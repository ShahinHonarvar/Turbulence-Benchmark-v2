from itertools import combinations

def lists_with_product_equal_n(lst):
    n = 990
    lst = lst + lst
    size = len(lst) // 2
    sublists = []
    for r in range(2, size + 1):
        for i in range(size):
            for c in combinations(lst[i:i + size], r):
                if all((x != 0 for x in c)) and n % c[0] == 0 and all((n // x in c for x in c[1:])):
                    sublists.append(list(c))
    return sublists