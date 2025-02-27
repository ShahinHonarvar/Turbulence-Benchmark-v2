def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) <= len(nums) and all((isinstance(x, int) for x in sublist)) and (29 == reduce(lambda x, y: x * y, sublist, 1)):
                result.append(sublist)
    return result