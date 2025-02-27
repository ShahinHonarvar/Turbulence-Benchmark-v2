def all_pos_ints_inclusive(nums):
    result = []
    for i in range(1, 9):
        if i >= 0 and i < len(nums) and (nums[i] > 0):
            result.append(nums[i])
    return result