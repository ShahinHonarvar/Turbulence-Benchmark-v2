from math import prod

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst *= 2
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            if prod(lst[i:j]) == -81:
                result.append(lst[i:j])
    return result