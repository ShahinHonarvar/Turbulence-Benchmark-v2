def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            product = 1
            sublist = nums[i:j + 1]
            for num in sublist:
                product *= num
            if product == 733:
                result.append(sublist)
    return result