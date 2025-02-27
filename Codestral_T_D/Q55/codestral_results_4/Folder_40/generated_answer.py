from itertools import product

def lists_with_product_equal_n(lst):
    n = -9
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if product(sublist) == n:
                result.append(sublist)
    return result