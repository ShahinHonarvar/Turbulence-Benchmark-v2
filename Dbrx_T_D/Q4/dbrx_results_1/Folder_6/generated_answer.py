def all_pos_ints_exclusive(nums):
    if len(nums) < 99:
        return []
    result = []
    for i in range(86, 99):
        if nums[i] > 0:
            result.append(nums[i])
    return result