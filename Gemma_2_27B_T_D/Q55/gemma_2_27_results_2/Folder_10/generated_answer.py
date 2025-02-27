def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if len(sublist) == 0:
                break
            product = 1
            for num in sublist:
                product *= num
            if product == -93:
                result.append(sublist)
    return result