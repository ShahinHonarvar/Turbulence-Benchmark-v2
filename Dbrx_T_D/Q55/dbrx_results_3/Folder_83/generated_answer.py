from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    n = -57
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if list(comb)[0] != list(comb)[-1]:
                continue
            if prod(comb) == n:
                result.append(list(comb))
    return result

def prod(lst):
    if lst:
        return reduce(lambda x, y: x * y, lst)
    else:
        return 1