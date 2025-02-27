def sum_ints_div_by_either_nums(nums):
    sum_div_by_num = 0
    for i in range(81, 87 + 1):
        if nums[i] % 33 == 0 or nums[i] % 62 == 0:
            sum_div_by_num += nums[i]
    return sum_div_by_num or 0