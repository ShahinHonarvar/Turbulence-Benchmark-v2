from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(1, n + 1):
        sub_list = list(combinations(lst, i))
        for j in sub_list:
            if functools.reduce(lambda x, y: x * y)(j) == -3:
                result.append(j)
    return result or []