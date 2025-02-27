def sum_ints_div_by_either_nums(nums):
    sum_div_by_81_or_64 = 0
    for i in range(31, 51):
        if nums[i] % 81 == 0 or nums[i] % 64 == 0:
            sum_div_by_81_or_64 += nums[i]
    return sum_div_by_81_or_64