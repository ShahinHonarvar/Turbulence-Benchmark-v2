def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:]
            if len(sublist) > 0 and all([num != 0 for num in sublist]) and (reduce(lambda x, y: x * y, sublist) == 93):
                result.append(sublist)
    return result