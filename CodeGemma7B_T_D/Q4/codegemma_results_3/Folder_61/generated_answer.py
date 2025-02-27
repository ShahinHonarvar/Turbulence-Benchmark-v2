def all_pos_ints_exclusive(nums):
    result = []
    for i in range(8):
        if i >= 1 and i <= 7 and (nums[i] > 0):
            result.append(i)
    return result