def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if 45 == prod(nums[i:j + 1]):
                result.append(nums[i:j + 1])
    for i in range(len(nums)):
        for j in range(i):
            if 45 == prod(nums[i:] + nums[:j + 1]):
                result.append(nums[i:] + nums[:j + 1])
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p