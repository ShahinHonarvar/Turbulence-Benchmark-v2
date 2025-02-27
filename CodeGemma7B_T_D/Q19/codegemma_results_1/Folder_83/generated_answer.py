def all_ints_not_div_by_num(nums):
    res = []
    for i in range(90, 200):
        if nums[i] % -31 != 0:
            res.append(nums[i])
    return res