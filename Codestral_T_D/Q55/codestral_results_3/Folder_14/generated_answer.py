from collections import deque

def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = deque(nums + nums)
    ans = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= nums[j]
            sublist.append(nums[j])
            if product == -72:
                ans.append(sublist)
            if product == 0:
                break
    return ans