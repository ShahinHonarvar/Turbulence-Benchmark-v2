def all_pos_ints_exclusive(nums):
    result = []
    for i in range(14, 66):
        if i < len(nums) and nums[i] > 0:
            result.append(nums[i])
    return result