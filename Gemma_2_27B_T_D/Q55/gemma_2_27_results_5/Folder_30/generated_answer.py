def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            product = 1
            sublist = nums[i:j + 1]
            for num in sublist:
                product *= num
            if product == 99:
                result.append(sublist)
    return result