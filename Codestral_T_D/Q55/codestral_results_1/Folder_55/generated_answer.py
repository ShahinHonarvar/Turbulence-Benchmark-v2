from collections import deque

def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = deque(nums + nums)
    result = []
    for _ in range(n):
        for i in range(1, n + 1):
            if i == 1:
                if nums[0] == -6:
                    result.append([nums[0]])
            else:
                product = 1
                for j in range(i):
                    product *= nums[j]
                    if product == -6:
                        result.append(list(nums[j - i + 1:j + 1]))
        nums.popleft()
    return result