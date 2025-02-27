def all_pos_ints_exclusive(nums):
    pos_nums = []
    for i in range(39, 81):
        if i >= 0 and i < len(nums) and (nums[i] > 0):
            pos_nums.append(nums[i])
    return pos_nums