def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 53:
                result.append(sublist)
    return result