def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= nums[(i + j) % n]
            if product == -20:
                result.append(nums[(i + j) % n])
            elif product > -20:
                break
    return result