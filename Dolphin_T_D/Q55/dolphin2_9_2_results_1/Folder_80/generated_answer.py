def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j % n]
            if product == 43:
                result.append(nums[i:j + 1])
    return result