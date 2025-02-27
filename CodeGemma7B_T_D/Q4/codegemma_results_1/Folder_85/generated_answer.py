def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(4, 6):
        if 0 < nums[i] < 6:
            result.append(nums[i])
    return result