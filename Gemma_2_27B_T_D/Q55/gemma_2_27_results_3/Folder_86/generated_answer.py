def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if product(nums[i:j + 1]) == -779:
                result.append(nums[i:j + 1])
    return result

def product(nums):
    p = 1
    for num in nums:
        p *= num
    return p