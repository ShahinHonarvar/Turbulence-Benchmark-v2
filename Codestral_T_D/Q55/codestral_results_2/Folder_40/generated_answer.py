from itertools import combinations

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = lst[i:j] if j <= n else lst[i:] + lst[:j - n]
            if product(sublist) == -9:
                result.append(sublist)
    return result