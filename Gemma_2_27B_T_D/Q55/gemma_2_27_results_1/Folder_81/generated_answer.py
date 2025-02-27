def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i:j + 1] not in sublists and all([x != 0 for x in nums[i:j + 1]]) and (reduce(lambda x, y: x * y, nums[i:j + 1]) == -8):
                sublists.append(nums[i:j + 1])
    return sublists