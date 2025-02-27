def all_pos_ints_inclusive(nums):
    result = []
    for i in range(56, 58):
        if i >= 0 and nums[i] >= 0:
            result.append(nums[i])
    return result