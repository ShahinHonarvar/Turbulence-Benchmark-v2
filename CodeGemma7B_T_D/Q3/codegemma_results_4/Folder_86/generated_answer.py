def all_pos_ints_inclusive(nums):
    result = []
    for i in range(31, 35):
        if 0 < nums[i] <= 10:
            result.append(nums[i])
    return result