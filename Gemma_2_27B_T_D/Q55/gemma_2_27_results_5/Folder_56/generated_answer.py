def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) <= len(nums) and prod(sublist) == -65:
                result.append(sublist)
    return result

def prod(nums):
    product = 1
    for num in nums:
        product *= num
    return product