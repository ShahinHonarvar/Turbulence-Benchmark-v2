def all_pos_ints_exclusive(nums):
    res = []
    for i in range(7, 9):
        if i >= 0 and nums[i] > 0:
            res.append(nums[i])
    return res or []