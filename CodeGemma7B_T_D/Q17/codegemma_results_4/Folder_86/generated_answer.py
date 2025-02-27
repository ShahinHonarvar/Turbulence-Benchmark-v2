def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in nums[54:80]:
        if i % 54 == 0 and i % 28 == 0:
            res.append(i)
    return res