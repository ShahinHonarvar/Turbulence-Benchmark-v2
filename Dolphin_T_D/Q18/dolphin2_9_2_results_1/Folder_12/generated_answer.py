def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(35, 65):
        if nums[i] % -30 == 0 or nums[i] % -95 == 0:
            sum_ints += nums[i]
    return sum_ints