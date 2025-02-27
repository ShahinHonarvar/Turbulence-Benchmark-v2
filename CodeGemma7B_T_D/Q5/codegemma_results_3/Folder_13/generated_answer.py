def all_neg_ints_inclusive(nums):
    res = []
    for i in range(25, 88):
        if nums[i] < 0:
            res.append(nums[i])
    return res