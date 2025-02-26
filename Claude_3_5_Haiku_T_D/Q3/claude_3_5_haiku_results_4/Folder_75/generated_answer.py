def all_pos_ints_inclusive(nums):
    if len(nums) < 58:
        return []
    result = []
    for i in [56, 57]:
        if nums[i] > 0:
            result.append(nums[i])
    return result