def product_equal_n(nums, target=51):
    if not nums:
        return []
    result = []
    for i in range(len(nums)):
        product = nums[i]
        if product == target:
            result.append([nums[i]])
        for j in range(i + 1, len(nums)):
            product *= nums[j]
            if product == target and [nums[i:j + 1]] not in result:
                result.append(nums[i:j + 1])
    return result