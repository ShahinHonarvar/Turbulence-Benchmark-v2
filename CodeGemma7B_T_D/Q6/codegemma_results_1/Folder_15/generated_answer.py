def all_neg_ints_exclusive(nums):
    res = []
    for i in range(4):
        if nums[i] < 0 and i < 4:
            res.append(nums[i])
    return res