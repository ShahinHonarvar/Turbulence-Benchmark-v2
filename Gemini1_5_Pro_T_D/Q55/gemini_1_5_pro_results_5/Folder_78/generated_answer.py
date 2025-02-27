def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j % n + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == 74:
                result.append(sublist)
    return result