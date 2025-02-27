from itertools import combinations

def lists_with_product_equal_n(numbers):
    result = []
    n = 537
    for i in range(1, len(numbers) + 1):
        for combo in combinations(numbers, i):
            if functools.reduce(lambda a, b: a * b, combo) == n:
                result.append(list(combo))
    return result