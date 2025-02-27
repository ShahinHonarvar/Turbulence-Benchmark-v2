def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(34, 70):
        if nums[i] % 19 == 0 or nums[i] % 32 == 0:
            sum += nums[i]
    return sum or 0