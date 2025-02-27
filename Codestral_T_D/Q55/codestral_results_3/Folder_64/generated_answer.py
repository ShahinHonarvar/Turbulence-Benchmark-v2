import itertools

def lists_with_product_equal_n(nums):
    n = 3
    result = []
    for r in range(1, len(nums) + 1):
        for i in range(len(nums)):
            for subset in itertools.combinations(nums[i:] + nums[:i], r):
                if subset.count(1) == len(subset) - subset.count(n):
                    result.append(list(subset))
    return result