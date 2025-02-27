def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(50, 200 + 1):
        if nums[i] % 34 == 0 or nums[i] % 64 == 0:
            total_sum += nums[i]
    return total_sum if total_sum > 0 else 0