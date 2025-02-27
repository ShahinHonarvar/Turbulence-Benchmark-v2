def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, len(nums)):
            product *= nums[j]
            sublist.append(nums[j])
            if product == 32:
                result.append(sublist.copy())
        for j in range(0, i):
            product *= nums[j]
            sublist.append(nums[j])
            if product == 32:
                result.append(sublist.copy())
    return result