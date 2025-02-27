def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if 86 <= num <= 99:
            total_sum += num
    if total_sum == 0:
        return 0
    return total_sum