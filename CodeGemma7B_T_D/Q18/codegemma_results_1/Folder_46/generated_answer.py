def sum_ints_div_by_either_nums(nums):
    sum_div_by_55_or_36 = 0
    for i in range(11, 47):
        if nums[i] % 55 == 0 or nums[i] % 36 == 0:
            sum_div_by_55_or_36 += nums[i]
    return sum_div_by_55_or_36