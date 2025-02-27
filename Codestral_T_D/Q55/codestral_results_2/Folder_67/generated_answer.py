def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= nums[j % n]
            sublist.append(nums[j % n])
            if product == 33:
                result.append(sublist)
    return result