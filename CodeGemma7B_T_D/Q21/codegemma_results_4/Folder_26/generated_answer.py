def all_ints_div_by_num(nums):
    res = []
    for i in range(45, 81):
        if nums[i] % 39 == 0:
            res.append(nums[i])
    return res