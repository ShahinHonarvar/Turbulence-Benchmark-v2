def all_pos_ints_inclusive(nums):
    if len(nums) <= 57:
        return []
    result = []
    for index in range(56, 58):
        if nums[index] > 0:
            result.append(nums[index])
    return result