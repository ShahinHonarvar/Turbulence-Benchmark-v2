def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(306, 958):
        if nums[i] % 982 == 0 or nums[i] % 319 == 0:
            total += nums[i]
    return total