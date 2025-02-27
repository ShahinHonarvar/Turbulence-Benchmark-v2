def all_pos_ints_exclusive(nums):
    result = []
    for i in range(12, 76):
        if i in range(len(nums)) and nums[i] > 0:
            result.append(nums[i])
    return result