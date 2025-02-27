def all_pos_ints_exclusive(nums):
    result = []
    for i in range(112, 473):
        if i < len(nums) and nums[i] > 0:
            result.append(nums[i])
    return result