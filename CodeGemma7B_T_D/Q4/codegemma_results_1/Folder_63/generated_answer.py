def all_pos_ints_exclusive(nums):
    result = []
    for i in range(38, 53):
        if i < len(nums) and nums[i] > 0:
            result.append(i)
    return result