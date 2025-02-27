def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:j + 1]
            if 1 in sublist:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == 91:
                result.append(sublist)
    return result