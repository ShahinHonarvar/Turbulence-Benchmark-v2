def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if 4 <= num <= 6:
            total_sum += num
    return total_sum or 0