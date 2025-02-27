def all_pos_ints_exclusive(nums):
    res = []
    for i in range(369, 984):
        if i in nums and i > 0 and (i != 476):
            res.append(i)
    return res