def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(48, 60):
        if nums[i] % 58 == 0 or nums[i] % 88 == 0:
            sum_nums += nums[i]
    return sum_nums if sum_nums != 0 else 0