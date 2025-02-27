def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) > 1 and reduce(lambda x, y: x * y, sublist) == 57:
                result.append(sublist)
            if j == len(nums) - 1:
                sublist = nums[i:] + nums[:i]
                if reduce(lambda x, y: x * y, sublist) == 57:
                    result.append(sublist)
    return result