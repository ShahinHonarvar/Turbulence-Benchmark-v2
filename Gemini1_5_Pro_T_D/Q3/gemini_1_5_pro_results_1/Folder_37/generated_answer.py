def all_pos_ints_inclusive(nums):
    result = []
    for i in range(1, 6):
        if i >= 1 and i < len(nums) and (nums[i] > 0):
            result.append(nums[i])
    return result