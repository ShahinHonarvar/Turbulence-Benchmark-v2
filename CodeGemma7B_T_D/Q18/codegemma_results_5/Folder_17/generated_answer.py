def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i in range(81, 90):
        if nums[i] % 56 == 0 or nums[i] % 68 == 0:
            sum_divisible += nums[i]
    return sum_divisible or 0