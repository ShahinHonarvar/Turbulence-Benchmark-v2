from collections import deque

def lists_with_product_equal_n(nums):
    nums = deque(nums)
    n = len(nums)
    result = []
    for _ in range(n):
        product = 1
        for j in range(n):
            product *= nums[j]
            if product == -46:
                result.append(list(nums[:j + 1]))
        nums.rotate(-1)
    return result