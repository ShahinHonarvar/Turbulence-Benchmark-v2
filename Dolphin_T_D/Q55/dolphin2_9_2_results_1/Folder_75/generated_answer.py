from itertools import combinations

def product(nums):
    p = 1
    for n in nums:
        p *= n
    return p

def lists_with_product_equal_n(nums):
    nums = list(nums) + list(nums)
    n = len(nums)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n):
            if product(nums[i:j]) == 13:
                sublists.append(nums[i:j])
    sublists = [s for s in sublists if len(s) <= n]
    return sublists