from itertools import combinations

def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if i <= j:
                sublist = lst[i:j]
            else:
                sublist = lst[i:] + lst[:j]
            if sublist and product(sublist) == -15:
                result.append(sublist)
    return result

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p