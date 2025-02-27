from collections import deque

def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    nums = nums + nums
    for i in range(n):
        product = 1
        sublist = deque()
        for j in range(i, n + i):
            product *= nums[j]
            sublist.append(nums[j])
            if product == -7:
                result.append(list(sublist))
            while product % 7 == 0 and len(sublist) > 1:
                product //= sublist.popleft()
                if product == -7:
                    result.append(list(sublist))
    return result