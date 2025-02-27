def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -57:
                result.append(sublist)
    for i in range(len(nums)):
        j = 0
        while j <= i:
            sublist = nums[i:j + 1] + nums[:i + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -57:
                result.append(sublist)
            j += 1
    return result