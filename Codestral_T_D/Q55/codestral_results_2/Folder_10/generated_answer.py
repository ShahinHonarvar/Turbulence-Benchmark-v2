from collections import deque

def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = deque(nums)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, n + i):
            product *= nums[j % n]
            sublist.append(nums[j % n])
            if product == -93:
                result.append(sublist)
            if product == 0:
                break
    return result