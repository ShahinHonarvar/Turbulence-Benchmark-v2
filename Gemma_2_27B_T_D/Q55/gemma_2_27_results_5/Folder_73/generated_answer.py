def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) > 1 and 40 == (sublist[0] if len(sublist) == 1 else sublist[0] * sublist[1]) * (sublist[2] if len(sublist) > 2 else 1):
                result.append(sublist)
    return result