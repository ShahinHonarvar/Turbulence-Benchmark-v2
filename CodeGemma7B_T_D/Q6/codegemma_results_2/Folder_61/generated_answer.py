def all_neg_ints_exclusive(nums):
    res = []
    for i in range(len(nums)):
        if -8 < nums[i] < -1:
            res.append(nums[i])
    return res