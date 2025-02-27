from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = 537
    result = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if reduce(lambda x, y: x * y, comb) == n:
                result.append(list(comb))
                break
    return result