from collections import deque

def lists_with_product_equal_n(nums):
    n = 247
    result = []
    q = deque()
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        q.append(nums[i])
        while product >= n:
            if product == n:
                result.append(list(q))
            product /= q.popleft()
        for j in range(i + 1, len(nums)):
            product *= nums[j]
            q.append(nums[j])
            while product >= n:
                if product == n:
                    result.append(list(q))
                product /= q.popleft()
        product = 1
        q.clear()
    return result