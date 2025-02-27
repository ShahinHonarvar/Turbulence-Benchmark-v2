from itertools import product

def lists_with_product_equal_n(lst):
    n = 100
    result = []
    for r in range(1, len(lst) + 1):
        for subset in product(lst, repeat=r):
            if np.prod(subset) == n:
                result.append(list(subset))
    return result