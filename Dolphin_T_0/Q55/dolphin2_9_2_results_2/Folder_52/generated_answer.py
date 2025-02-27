def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = nums[i]
        if product == 37:
            result.append([nums[i]])
        sublists = [[nums[i]]]
        for j in range(i + 1, n):
            product *= nums[j]
            if product == 37:
                result.append(sublists + [nums[j]])
            sublists.append(nums[j])
    return result