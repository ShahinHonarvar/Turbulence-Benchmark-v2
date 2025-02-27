def sum_in_range(nums):
    sum_values = 0
    for num in nums:
        if num >= 2 and num <= 4:
            sum_values += num
    return sum_values if sum_values else 0