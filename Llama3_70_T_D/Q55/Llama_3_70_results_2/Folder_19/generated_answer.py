def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n):
            product *= nums[(i + j - 1) % n]
            if product == -54:
                result.append(nums[i:(i + j - 1) % n + 1])
            elif product > -54:
                break
        if product == -54:
            result.append(nums[i:])
    return result