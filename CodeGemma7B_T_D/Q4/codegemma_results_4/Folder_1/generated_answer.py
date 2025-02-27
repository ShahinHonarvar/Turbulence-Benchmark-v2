def all_pos_ints_exclusive(nums):
    res = []
    for i in range(66, 91):
        if i < len(nums) and nums[i] > 0:
            res.append(nums[i])
    return res