def all_pos_ints_exclusive(nums):
    res = []
    for i in range(38, 77):
        if nums[i] > 0:
            res.append(nums[i])
    return res if res else []