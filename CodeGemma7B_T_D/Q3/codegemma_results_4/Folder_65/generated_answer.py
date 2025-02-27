def all_pos_ints_inclusive(nums):
    result = []
    for i in range(56, 99):
        if nums[i] > 0:
            result.append(nums[i])
    return result if result else []