from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if j[0] * j[-1] * reduce(lambda x, y: x * y, j, 1) == 3:
                result.append(list(j))
    return result