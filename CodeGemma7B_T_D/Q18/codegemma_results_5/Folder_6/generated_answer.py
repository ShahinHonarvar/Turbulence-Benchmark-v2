def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(41, 57):
        if nums[i] % 82 == 0 or nums[i] % 90 == 0:
            total_sum += nums[i]
    return total_sum if total_sum else 0