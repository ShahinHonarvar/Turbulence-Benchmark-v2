from sympy import *

def generate_subarrays_with_product(n, lst, i=0):
    result = []
    if i == len(lst):
        return []
    product = lst[i]
    if product == n:
        result.append([lst[i]])
    for j in range(i + 1, len(lst) + i):
        product *= lst[j % len(lst)]
        if product == n:
            result.append([lst[i], lst[j % len(lst)]])
        if product < n:
            result += generate_subarrays_with_product(n, lst, j)
        if product > n:
            break
    return result

def partsets(lst):
    if len(lst) == 0:
        [[]]
    else:
        [[x] + p for i, x in enumerate(lst) for p in partsets(lst[:i] + lst[i + 1:])]

def lists_with_product_equal_n(lst):
    result = []
    n = 54
    subsets = partsets(lst)
    for subset in subsets:
        result += generate_subarrays_with_product(n, subset)
    return list(set(tuple(result)))