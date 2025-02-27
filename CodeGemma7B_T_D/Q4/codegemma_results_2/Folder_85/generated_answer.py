def all_pos_ints_exclusive(nums):
    res = []
    for i in nums[4:5]:
        if i > 0:
            res.append(i)
    return res or []