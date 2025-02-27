def lists_with_product_equal_n(nums):
    if not nums:
        return []
    result = []
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
    if product == -76:
        result.append(nums)
    if len(nums) > 1:
        for i in range(len(nums)):
            new_nums = nums[i + 1:] + nums[:i]
            result += lists_with_product_equal_n(new_nums)
    return result