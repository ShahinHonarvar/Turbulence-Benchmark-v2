def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            for k in range(j + 1, n + 1):
                if nums[i:j] + nums[j:k] and prod(nums[i:j] + nums[j:k]) == -46:
                    result.append(nums[i:j] + nums[j:k])
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p