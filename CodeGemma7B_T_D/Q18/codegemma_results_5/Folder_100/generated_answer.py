def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(72, 94):
        if nums[i] % 32 == 0 or nums[i] % 44 == 0:
            total_sum += nums[i]
    return total_sum