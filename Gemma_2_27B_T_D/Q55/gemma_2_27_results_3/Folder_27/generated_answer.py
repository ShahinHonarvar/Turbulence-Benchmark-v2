def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j + 1]
            if len(sublist) > 0 and reduce(lambda x, y: x * y, sublist) == -82:
                result.append(sublist)
    return result