def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + i + 1):
            sublist = nums[i:j]
            if len(sublist) <= len(nums) and product(sublist) == -779:
                result.append(sublist)
    return result

def product(nums):
    p = 1
    for num in nums:
        p *= num
    return p