def all_neg_ints_exclusive(nums):
    if not nums or len(nums) < 41:
        return []
    result = []
    for i in range(42, 70):
        if nums[i] < 0:
            result.append(nums[i])
    return result