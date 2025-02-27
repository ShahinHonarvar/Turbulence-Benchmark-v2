from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for sub_list in combinations(lst, i):
            if reduce(lambda x, y: x * y, sub_list, 1) == -23:
                result.append(list(sub_list))
    return result