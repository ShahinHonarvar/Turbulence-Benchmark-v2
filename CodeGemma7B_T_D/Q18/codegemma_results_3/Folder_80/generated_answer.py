def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(14, 94):
        if nums[i] % 71 == 0 or nums[i] % 81 == 0:
            sum_nums += nums[i]
    return sum_nums