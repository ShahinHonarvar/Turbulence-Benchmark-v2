def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subset = nums[i:j + 1]
            product = 1
            for num in subset:
                product *= num
            if product == -1:
                result.append(subset)
    return result