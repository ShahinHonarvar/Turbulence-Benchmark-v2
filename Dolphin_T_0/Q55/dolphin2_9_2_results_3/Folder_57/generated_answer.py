from itertools import combinations, compress
	from functools import reduce
	import operator

def lists_with_product_equal_n(n, arr):
    n = reduce(operator.mul, arr, 1) // n
    results = []
    length = len(arr)
    for i in range(length):
        zo = list(combinations(arr, i + 1))
        zo = [z for z in zo if reduce(operator.mul, z, 1) % n == 0]
        for z in zo:
            if reduce(operator.mul, z, 1) // n == 1:
                results.append(z)
    return results