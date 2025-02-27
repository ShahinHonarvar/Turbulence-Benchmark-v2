def all_neg_ints_exclusive(nums):
    if len(nums) < 75:
        return []
    result = []
    for i in range(49, 74):
        if nums[i] < 0:
            result.append(nums[i])
    return result