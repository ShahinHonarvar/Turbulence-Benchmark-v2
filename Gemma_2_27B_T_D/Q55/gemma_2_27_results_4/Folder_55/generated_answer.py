def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if product(nums[i:j + 1]) == -6:
                result.append(nums[i:j + 1])
    return result

def product(nums):
    p = 1
    for x in nums:
        p *= x
    return p