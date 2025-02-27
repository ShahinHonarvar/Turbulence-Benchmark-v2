def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) > 0 and reduce(lambda x, y: x * y, sublist) == -51:
                result.append(sublist)
    return result