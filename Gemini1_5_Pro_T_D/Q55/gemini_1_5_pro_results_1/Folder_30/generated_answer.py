def lists_with_product_equal_n(nums):
    n = len(nums)
    if n == 0:
        return []
    extended_nums = nums * 2
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = extended_nums[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == 99:
                result.append(sublist)
    return result