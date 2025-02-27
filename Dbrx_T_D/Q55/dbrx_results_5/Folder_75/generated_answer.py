from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for sublst in combinations(lst, i):
            if isinstance(sublst, int):
                sublst = [sublst]
            if sublst[0] * product(sublst[1:]) == 13 and sublst not in result:
                result.append(sublst)
    return result

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result