def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums * 2
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j]
            if product == -91:
                result.append(nums[i:j + 1])
    return result