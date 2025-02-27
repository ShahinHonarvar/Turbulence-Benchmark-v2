def sum_in_range(nums):
    total_sum = 0
    for num in nums:
        if -9 <= num <= -7:
            total_sum += num
    if total_sum == 0:
        return 0
    else:
        return total_sum