def all_ints_div_by_num(nums):
    l, r, res = (31, 67, [])
    for i in range(l, r + 1):
        if nums[i] % -15 == 0:
            res.append(nums[i])
    return res if res else []