def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i in range(90, 98):
        if nums[i] % 13 == 0 or nums[i] % 35 == 0:
            sum_divisible += nums[i]
    return sum_divisible or 0