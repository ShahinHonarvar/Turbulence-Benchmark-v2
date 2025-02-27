def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(2, 7 + 1):
        if nums[i] % -1 == 0 or nums[i] % -7 == 0:
            sum_nums += nums[i]
    return sum_nums