def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) > 1 and sublist[-1] == nums[0]:
                sublist.append(nums[0])
            product = 1
            for num in sublist:
                product *= num
            if product == 93:
                result.append(sublist)
    return result