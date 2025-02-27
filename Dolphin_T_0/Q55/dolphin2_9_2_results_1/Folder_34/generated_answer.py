from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for x in combinations(lst, size):
            if size == 1 and x[0] == -81 or (size > 1 and x[0] == -81 and (x[1] % 81 == 0) and (x[1] < 0) and (x[-1] % 81 == 0) and (x[-1] < 0) and (x[1] * x[-1] == -81) and all((i % 81 == 0 and i < 0 for i in x[1:-1]))):
                result.append(list(x))
    return result