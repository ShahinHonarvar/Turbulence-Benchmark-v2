def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if 15 <= num <= 57:
            total_sum += num
    return total_sum or 0