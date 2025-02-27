def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(35, 65):
        if nums[i] % 30 == 0 or nums[i] % 95 == 0:
            s += nums[i]
    return s or 0