def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + i + 1):
            if nums[i:j % len(nums)] and prod(nums[i:j % len(nums)]) == -93:
                result.append(nums[i:j % len(nums)])
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p