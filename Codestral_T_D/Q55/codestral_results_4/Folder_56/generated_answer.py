from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    n = -65
    res = []
    for i in range(len(nums)):
        if nums[i] == n:
            res.append([nums[i]])
            continue
        prod = nums[i]
        for j in range(i + 1, len(nums) + i):
            if prod == n:
                res.append(nums[i:j % len(nums)] if i < j % len(nums) else nums[i:] + nums[:j % len(nums)])
            if j - i < len(nums):
                prod *= nums[j % len(nums)]
    return res