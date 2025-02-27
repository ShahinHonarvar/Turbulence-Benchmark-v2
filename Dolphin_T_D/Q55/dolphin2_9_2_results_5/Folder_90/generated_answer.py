from itertools import combinations

def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums) + 1):
        for subset in combinations(nums, i):
            product = 1
            for number in subset:
                product *= number
            if product == -690:
                result.append(list(subset))
    return result