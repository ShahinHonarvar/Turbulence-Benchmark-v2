def lists_with_product_equal_n(nums, n=51):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product == n:
                result.append(nums[i:j + 1])
    return result