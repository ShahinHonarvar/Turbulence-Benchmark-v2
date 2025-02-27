def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            if nums[i:j + 1] and eval('*'.join((str(x) for x in nums[i:j + 1]))) == -97:
                result.append(nums[i:j + 1])
    return result