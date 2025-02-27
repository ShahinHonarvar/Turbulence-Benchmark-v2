def sum_ints_div_by_either_nums(nums):
    sum_div_nums = 0
    for i in range(828, 933):
        if nums[i] % -649 == 0 or nums[i] % -461 == 0:
            sum_div_nums += nums[i]
    return sum_div_nums