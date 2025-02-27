def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j % n + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 48:
                result.append(sublist)
    return result