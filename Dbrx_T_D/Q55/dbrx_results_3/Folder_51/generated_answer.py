from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = -44
    if n == 0:
        return [sublist for sublist in circular_list if sublist == [0]]
    if n < 1:
        sublists = []
        for size in range(1, len(circular_list) + 1):
            sublists.extend(list(combinations(circular_list, size)))
        return [sublist for sublist in sublists if reduce(lambda x, y: x * y, sublist) == n and sublist != [-1, 1]]
    else:
        sublists = []
        for size in range(1, len(circular_list) + 1):
            sublists.extend(list(combinations(circular_list, size)))
        return [sublist for sublist in sublists if reduce(lambda x, y: x * y, sublist) == n]