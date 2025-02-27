def all_pos_ints_inclusive(nums):
    if len(nums) < 8:
        return []
    result = []
    for i in range(5, 8):
        if nums[i] > 0:
            result.append(nums[i])
    return result