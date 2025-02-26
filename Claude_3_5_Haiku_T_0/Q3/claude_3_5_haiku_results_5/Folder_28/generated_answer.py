def all_pos_ints_inclusive(nums):
    if len(nums) < 64:
        return []
    result = []
    for i in [62, 63]:
        if nums[i] > 0:
            result.append(nums[i])
    return result