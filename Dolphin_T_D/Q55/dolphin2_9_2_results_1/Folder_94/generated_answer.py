def lists_with_product_equal_n(nums, n):
    result = []
    p = 1
    start = 0
    for end in range(len(nums)):
        p *= nums[end]
        while p > n and start < end:
            p /= nums[start]
            start += 1
        if p == n:
            result.append(nums[start:end + 1])
    return result