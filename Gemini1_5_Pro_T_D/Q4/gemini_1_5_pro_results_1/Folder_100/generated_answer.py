def all_pos_ints_exclusive(nums):
    result = []
    for i in range(23, 24):
        if i >= 0 and i < len(nums) and (nums[i] > 0):
            result.append(nums[i])
    return result