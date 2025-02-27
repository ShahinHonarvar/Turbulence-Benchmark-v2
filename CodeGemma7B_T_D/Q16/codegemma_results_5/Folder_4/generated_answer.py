def sum_even_ints_inclusive(nums):
    start_idx = 12
    end_idx = 92
    total_sum = 0
    for i in range(start_idx, end_idx + 1):
        if nums[i] % 2 == 0:
            total_sum += nums[i]
    return total_sum or 0