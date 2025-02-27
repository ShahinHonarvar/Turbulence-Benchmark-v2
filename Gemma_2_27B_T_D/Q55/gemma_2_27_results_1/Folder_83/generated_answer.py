def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if prod(nums[i:j + 1]) == -57:
                result.append(nums[i:j + 1])
            if j == len(nums) - 1:
                for k in range(i):
                    if prod(nums[i:j + 1] + nums[:k + 1]) == -57:
                        result.append(nums[i:j + 1] + nums[:k + 1])
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p