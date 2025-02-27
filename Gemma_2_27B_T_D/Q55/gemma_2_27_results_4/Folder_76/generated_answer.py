def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) <= len(nums) and 247 == eval('*'.join(map(str, sublist))):
                result.append(sublist)
    return result