def sum_ints_div_by_either_nums(nums):
    sum_div_by_nums = 0
    for i in range(80, 201):
        if nums[i] % 10 == 0 or nums[i] % 1000 == 0:
            sum_div_by_nums += nums[i]
    return sum_div_by_nums