from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = 42
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if n % j[-1] != 0:
                continue
            if n in [j[-1] * x for x in list(iter(j))]:
                result.append(list(j))
    return [list(circular_list[i:j]) for i, j in combinations(range(len(circular_list) + 1), 2) if circular_list[i:j] in result]