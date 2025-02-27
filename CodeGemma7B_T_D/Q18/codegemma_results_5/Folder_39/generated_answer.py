def sum_ints_div_by_either_nums(nums):
    sum_of_divisible = 0
    for i in range(13, 78):
        if nums[i] % 66 == 0 or nums[i] % 32 == 0:
            sum_of_divisible += nums[i]
    return sum_of_divisible