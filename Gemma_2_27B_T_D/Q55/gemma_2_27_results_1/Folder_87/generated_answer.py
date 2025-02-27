def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:]
            if len(sublist) > 0 and 1 == all((x != 0 for x in sublist)) and (27 == reduce(lambda x, y: x * y, sublist, 1)):
                result.append(sublist)
    return result