def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if num >= 38 and num <= 81:
            total_sum += num
    return total_sum