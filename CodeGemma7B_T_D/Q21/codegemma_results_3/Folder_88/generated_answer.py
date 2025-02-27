def all_ints_div_by_num(nums):
    res = []
    for x in nums[0:3]:
        if x % -8 == 0:
            res.append(x)
    return res