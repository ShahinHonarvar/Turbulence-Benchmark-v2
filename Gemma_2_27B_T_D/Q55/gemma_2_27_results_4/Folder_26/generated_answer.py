def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) > 1 and sublist[-1] * 93 / sublist[:-1].prod() == sublist[0]:
                result.append(sublist)
    return result