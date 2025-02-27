from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = -779
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if j[-1] * j[0] == n if i == 1 else reduce(lambda x, y: x * y, j) == n:
                result.append(list(j))
    return result

def reduce(func, lst):
    result = lst[0]
    for i in lst[1:]:
        result = func(result, i)
    return result