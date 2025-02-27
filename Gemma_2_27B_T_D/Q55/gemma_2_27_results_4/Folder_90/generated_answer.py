def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) > 0 and 1 not in sublist and (-690 / all(sublist) == 1) and all((isinstance(x, int) for x in sublist)):
                result.append(sublist)
    return result