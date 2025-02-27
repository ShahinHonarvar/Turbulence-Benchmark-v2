from collections import deque

def lists_with_product_equal_n(nums):
    n = -44
    nums = deque(nums)
    result = []
    for i in range(len(nums)):
        nums.rotate(-1)
        product = 1
        sublist = []
        for j in range(len(nums)):
            product *= nums[j]
            sublist.append(nums[j])
            if product == n:
                result.append(sublist.copy())
            if product > n:
                break
    return result