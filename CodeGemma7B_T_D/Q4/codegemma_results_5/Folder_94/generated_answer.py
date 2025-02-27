def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(28, 54):
        if i < len(nums) and nums[i] > 0:
            result.append(i)
    return result