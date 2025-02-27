def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if prod(nums[i:j]) == -26:
                result.append(nums[i:j])
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p