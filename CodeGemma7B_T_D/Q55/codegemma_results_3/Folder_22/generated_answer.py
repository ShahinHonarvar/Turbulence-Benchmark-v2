from itertools import combinations

def lists_with_product_equal_n(nums):
    for k in range(1, len(nums) + 1):
        for sublist in combinations(nums, k):
            if product(sublist) == 4:
                return sublist
    return []

def product(nums):
    result = 1
    for num in nums:
        result *= num
    return result