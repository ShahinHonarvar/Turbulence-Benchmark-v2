def all_pos_ints_exclusive(nums):
    res = []
    for i in range(20, 93):
        if nums[i] > 0:
            res.append(nums[i])
    return res