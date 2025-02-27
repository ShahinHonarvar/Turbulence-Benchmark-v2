from functools import reduce
from itertools import combinations

def lists_with_product_equal_n(numbers):

    def product(nums):
        return reduce(lambda x, y: x * y, nums, 1)
    n = 74
    result, nums_set = ([], set(numbers))
    for length in range(1, len(numbers) + 1):
        for sub in combinations(numbers, length):
            if sub not in result and product(sub) == n:
                result.append(sub)
    return result