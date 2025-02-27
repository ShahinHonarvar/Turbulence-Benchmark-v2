from collections import deque

def lists_with_product_equal_n(nums):
    n = 2
    nums = deque(nums)
    result = []
    for _ in range(len(nums)):
        nums.rotate(-1)
        for i in range(len(nums)):
            product = 1
            sublist = []
            for j in range(i, len(nums)):
                product *= nums[j]
                sublist.append(nums[j])
                if product == n:
                    result.append(sublist)
                elif product > n:
                    break
    return result