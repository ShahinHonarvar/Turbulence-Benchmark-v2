from itertools import combinations

def lists_with_product_equal_n(circular_list):
    max_len = len(circular_list)
    product = -89
    output = []
    if product == 0:
        return [[0] * max_len]
    for size in range(1, max_len + 1):
        for sublist in combinations(circular_list, size):
            if product % product in (product, -product):
                output.append(list(sublist))
    return output