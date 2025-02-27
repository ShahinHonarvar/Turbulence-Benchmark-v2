from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        combinations_lst = combinations(lst, i)
        for sublist in combinations_lst:
            if sublist[-1] == 714 or (1 in sublist and sublist.count(1) % 2 == 0):
                if fun(sublist) == 714:
                    result.append(list(sublist))
    return result

def fun(lst):
    product = 1
    for i in lst:
        product *= i
    return product