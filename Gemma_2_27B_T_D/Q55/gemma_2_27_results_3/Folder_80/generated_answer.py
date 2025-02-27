def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = nums[i:j % n]
            if len(sublist) > 0 and reduce(lambda x, y: x * y, sublist, 1) == 43:
                result.append(sublist)
    return result