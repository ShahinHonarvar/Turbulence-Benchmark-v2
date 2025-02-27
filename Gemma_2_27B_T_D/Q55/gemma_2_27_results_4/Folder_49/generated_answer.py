def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k % len(nums)]
            if product == -61:
                result.append(nums[i:j + 1])
    return result