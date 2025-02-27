def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(1, 9):
        if nums[i] % -9 == 0 and nums[i] % -3 == 0:
            res.append(nums[i])
    return res