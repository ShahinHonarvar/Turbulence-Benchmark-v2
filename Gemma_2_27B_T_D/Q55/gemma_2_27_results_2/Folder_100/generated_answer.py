def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if 48 == eval('*'.join((str(x) for x in nums[i:j + 1]))):
                result.append(nums[i:j + 1])
    return result