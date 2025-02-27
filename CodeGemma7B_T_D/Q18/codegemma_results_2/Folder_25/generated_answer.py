def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(25, 81):
        if nums[i] % 20 == 0 or nums[i] % 26 == 0:
            s += nums[i]
    return s if s else 0