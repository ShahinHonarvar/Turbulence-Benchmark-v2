def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(61, 89):
        if nums[i] % 31 == 0 or nums[i] % 11 == 0:
            sum_ints += nums[i]
    return sum_ints or 0