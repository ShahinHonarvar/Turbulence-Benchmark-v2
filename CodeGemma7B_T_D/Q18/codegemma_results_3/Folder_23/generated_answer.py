def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(69, 98):
        if nums[i] % -90 == 0 or nums[i] % -67 == 0:
            s += nums[i]
    return s