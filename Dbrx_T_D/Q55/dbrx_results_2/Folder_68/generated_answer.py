from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for j in combinations(lst, i):
            if j[0] != 0 and j[1] != 0 and (prod(j) == 6):
                result.append(list(j))
    return result

def prod(lst):
    product = 1
    for i in lst:
        product *= i
    return product