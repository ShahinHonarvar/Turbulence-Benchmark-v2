def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subset = nums[i:j]
            if len(subset) <= len(nums) and 37 in [x * y for x in subset for y in subset if x != y]:
                result.append(subset)
    return result