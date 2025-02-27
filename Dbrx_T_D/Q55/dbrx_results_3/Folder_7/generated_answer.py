from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(1, len(circular_list) + 1):
        for combo in combinations(circular_list, i):
            if reduce(lambda x, y: x * y, combo) == 537:
                result.append(list(combo))
    return result