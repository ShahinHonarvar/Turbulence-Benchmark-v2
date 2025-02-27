def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if i == 0:
                sublist = nums[i:j] + nums[:j]
            else:
                sublist = nums[i:j]
            if len(sublist) > 1 and reduce(lambda x, y: x * y, sublist) == -968:
                result.append(sublist)
    return result