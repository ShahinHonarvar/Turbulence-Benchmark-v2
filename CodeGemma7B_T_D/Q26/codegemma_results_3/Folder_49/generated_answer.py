def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if num >= 3 and num <= 9:
            total_sum += num
    return total_sum if total_sum else 0