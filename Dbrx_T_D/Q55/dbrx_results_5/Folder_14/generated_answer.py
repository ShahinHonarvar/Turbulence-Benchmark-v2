from itertools import islice, combinations

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        for j in combinations(numbers, i):
            if reduce(lambda x, y: x * y, j, 1) == -72:
                result.append(list(j))
    return result