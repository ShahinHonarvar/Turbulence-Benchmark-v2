def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums[:-1]
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k]
                if product > 83:
                    break
            if product == 83:
                result.append(nums[i:j + 1])
    return result