def all_ints_not_div_by_num(nums):
    res = []
    for i in range(36, 85):
        if nums[i] % -27 != 0:
            res.append(nums[i])
    if not res:
        return []
    return res