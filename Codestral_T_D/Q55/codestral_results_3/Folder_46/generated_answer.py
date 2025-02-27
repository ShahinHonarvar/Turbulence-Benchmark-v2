from itertools import combinations

def lists_with_product_equal_n(lst):
    double_lst = lst + lst
    n = len(lst)
    result = []
    for length in range(1, n + 1):
        for i in range(n):
            sublist = double_lst[i:i + length]
            if prod(sublist) == 53:
                result.append(sublist)
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p