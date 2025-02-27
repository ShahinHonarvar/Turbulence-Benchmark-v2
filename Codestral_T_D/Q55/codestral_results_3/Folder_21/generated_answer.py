def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums[:n - 1]
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i - 1):
            product *= nums[j]
            if product == 851:
                result.append(nums[i:j + 1])
            if product > 851:
                break
    return result