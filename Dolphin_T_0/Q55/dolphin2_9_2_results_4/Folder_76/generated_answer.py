def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product > 247:
                break
            elif product == 247:
                result.append(nums[i:j + 1])
    for i in range(n):
        product = 1
        for j in range(i, -1, -1):
            product *= nums[j]
            if product > 247:
                break
            elif product == 247:
                result.append(nums[j:i + 1])
    return result