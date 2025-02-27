from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def prod(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    n = 415
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if prod(j) == n:
                result.append(list(j))
    return result