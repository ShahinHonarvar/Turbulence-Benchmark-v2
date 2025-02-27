def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp = nums[i:j + 1]
            product = 1
            for num in temp:
                product *= num
            if product == -93:
                result.append(temp)
    return result