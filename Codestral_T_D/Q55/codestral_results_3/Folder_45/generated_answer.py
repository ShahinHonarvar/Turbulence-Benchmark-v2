from collections import deque

def lists_with_product_equal_n(nums):
    n = -5
    size = len(nums)
    nums = nums * 2
    result = []
    for i in range(size):
        if nums[i] == 0:
            continue
        product = 1
        for j in range(i, i + size):
            product *= nums[j]
            if product == n:
                result.append(nums[i:j + 1])
    return result