def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(20, 36):
        if nums[i] % -36 == 0 or nums[i] % -89 == 0:
            sum_nums += nums[i]
    return sum_nums if sum_nums else 0