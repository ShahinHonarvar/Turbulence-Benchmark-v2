def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(29, 46):
        if nums[i] % 27 == 0 or nums[i] % 81 == 0:
            sum_ints += nums[i]
    return sum_ints