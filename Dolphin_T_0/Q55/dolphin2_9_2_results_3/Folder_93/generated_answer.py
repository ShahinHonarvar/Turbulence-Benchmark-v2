def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    product_n = -91
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product == 0:
                result = []
                break
            if product == product_n:
                result.append(nums[i:j + 1])
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product == 0:
                result = []
                break
            if product == product_n:
                result.append(nums[:i] + nums[j + 1:])
    return result