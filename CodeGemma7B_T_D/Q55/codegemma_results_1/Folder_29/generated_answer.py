from itertools import chain, combinations

def lists_with_product_equal_n(arr, n=15):
    return chain(*(g for i in range(len(arr)) for j in range(i + 1, len(arr)) for g in combinations(arr[i:j + 1], len(arr[i:j + 1])) if product(g) == n))