from itertools import combinations, islice

def lists_with_product_equal_n(circular_list):
    n = -837
    result = []
    for i in range(1, len(circular_list) + 1):
        for sub_list in combinations(circular_list, i):
            if sub_list[0] * sub_list[1:] == n:
                result.append(list(sub_list))
    return result