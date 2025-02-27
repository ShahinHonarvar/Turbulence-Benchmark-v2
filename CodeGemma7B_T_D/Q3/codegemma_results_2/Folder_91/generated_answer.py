def all_pos_ints_inclusive(nums):
    result = []
    for i in range(6):
        if i >= 0 and i <= 5 and (nums[i] >= 1):
            result.append(nums[i])
    return result