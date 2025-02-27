def all_neg_ints_inclusive(nums):
    res = []
    for i in range(33, 37):
        if nums[i] < 0:
            res.append(nums[i])
    return res if res else []