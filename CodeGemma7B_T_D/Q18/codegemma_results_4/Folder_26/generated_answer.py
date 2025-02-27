def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(69, 71):
        if nums[i] % 72 == 0 or nums[i] % 70 == 0:
            s += nums[i]
    return s if s else 0