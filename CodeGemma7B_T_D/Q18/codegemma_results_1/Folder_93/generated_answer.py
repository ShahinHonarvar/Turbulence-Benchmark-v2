def sum_ints_div_by_either_nums(nums):
    sum_int = 0
    for i in range(86, 89 + 1):
        if nums[i] % -61 == 0 or nums[i] % -79 == 0:
            sum_int += nums[i]
    return sum_int