def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, len(nums)):
            product *= nums[j % len(nums)]
            sublist.append(nums[j % len(nums)])
            if product == -33:
                result.append(sublist.copy())
    return result