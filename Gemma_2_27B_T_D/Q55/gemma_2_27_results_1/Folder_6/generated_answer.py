def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if len(sublist) > 0 and reduce(lambda x, y: x * y, sublist) == 42:
                result.append(sublist)
    return result