from itertools import combinations_with_replacement as combinations

def lists_with_product_equal_n(lst):
    for i in range(1, len(lst) + 1):
        for sublist in combinations(lst, i):
            if sum(sublist) == 32:
                if sublist not in result:
                    result.append(sublist)
    if not result:
        return []
    return result