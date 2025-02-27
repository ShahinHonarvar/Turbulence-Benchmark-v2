def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if 60 <= num <= 90:
            total_sum += num
    return total_sum