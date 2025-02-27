from collections import deque

def lists_with_product_equal_n(nums):
    n = -779
    result = []
    nums = deque(nums)
    for _ in range(len(nums)):
        nums.rotate(-1)
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product == n:
                    result.append(list(nums)[i:j + 1])
                if abs(product) > abs(n):
                    break
    return result