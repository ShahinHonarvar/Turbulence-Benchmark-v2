def all_ints_div_by_num(nums):
    res = []
    for i in range(25, 42):
        if nums[i] % -97 == 0:
            res.append(nums[i])
    if len(res) == 0:
        return []
    return res