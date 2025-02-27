from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if not j or (len(j) > 1 and 0 in j):
                continue
            prod = 1
            for k in j:
                prod *= k
            if prod == 10:
                result.append(j)
    return result