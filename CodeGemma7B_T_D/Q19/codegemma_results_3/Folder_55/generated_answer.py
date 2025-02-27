def all_ints_not_div_by_num(nums):
    res = []
    for i in range(9):
        if nums[i] % 10 != 0:
            res.append(nums[i])
    return res