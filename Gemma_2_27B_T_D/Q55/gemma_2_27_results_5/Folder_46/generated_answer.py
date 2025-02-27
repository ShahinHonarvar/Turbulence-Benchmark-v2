def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i:j + 1] and 53 == eval('*'.join((str(k) for k in nums[i:j + 1]))):
                result.append(nums[i:j + 1])
    return result