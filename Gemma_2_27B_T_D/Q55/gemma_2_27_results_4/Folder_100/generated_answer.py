def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:]
            product = 1
            for num in sublist:
                product *= num
            if product == 48:
                result.append(sublist)
    return result