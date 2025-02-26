def all_pos_ints_inclusive(nums):
    if len(nums) < 64:
        return []
    result = []
    for i in range(62, 64):
        if nums[i] > 0:
            result.append(nums[i])
    return result