def lists_with_product_equal_n(nums):
    result = []
    nums_len = len(nums)
    product = 1
    for i in range(nums_len):
        product *= nums[i]
    if product != 100:
        return result
    product = 1
    for i in range(nums_len):
        product *= nums[i]
        if product == 100:
            for j in range(i + 1, nums_len + 1):
                product /= nums[i]
                if j < nums_len:
                    product *= nums[j]
                if product == 100:
                    result.append(nums[i:j + 1])
    return result