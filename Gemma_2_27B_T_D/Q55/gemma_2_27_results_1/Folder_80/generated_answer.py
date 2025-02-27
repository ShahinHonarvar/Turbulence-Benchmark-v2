def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp = nums[i:j + 1]
            product = 1
            for num in temp:
                product *= num
            if product == 43:
                result.append(temp)
    for i in range(len(nums)):
        for j in range(i):
            temp = nums[i:] + nums[:j]
            product = 1
            for num in temp:
                product *= num
            if product == 43:
                result.append(temp)
    return result