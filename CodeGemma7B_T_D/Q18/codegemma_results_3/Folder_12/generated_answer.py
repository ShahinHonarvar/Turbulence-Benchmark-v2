def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(35, 65):
        if nums[i] % 30 == 0 or nums[i] % 95 == 0:
            total_sum += nums[i]
    return total_sum or 0