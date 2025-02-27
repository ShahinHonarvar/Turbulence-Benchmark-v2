from itertools import combinations

def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst) // 2
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            if j - i > n:
                break
            if prod(lst[i:j]) == 6:
                result.append(lst[i:j])
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p