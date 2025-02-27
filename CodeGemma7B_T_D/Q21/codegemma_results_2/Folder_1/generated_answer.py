def all_ints_div_by_num(nums):
    res = []
    for x in nums[59:78]:
        if x % -95 == 0:
            res.append(x)
    return res or []