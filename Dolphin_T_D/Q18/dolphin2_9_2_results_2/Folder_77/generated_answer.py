def sum_ints_div_by_either_nums(nums):
    lower_bound = 828
    upper_bound = 932
    sum = 0
    for i in range(lower_bound, upper_bound + 1):
        if nums[i] % -649 == 0 or nums[i] % -461 == 0:
            sum += nums[i]
    return sum