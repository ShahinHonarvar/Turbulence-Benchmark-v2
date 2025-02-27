def sum_ints_div_by_either_nums(nums):
    sum_div = 0
    for i in range(34, 82):
        if nums[i] % 27 == 0 or nums[i] % 57 == 0:
            sum_div += nums[i]
    return sum_div