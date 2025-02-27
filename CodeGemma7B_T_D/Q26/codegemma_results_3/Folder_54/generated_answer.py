def sum_in_range(nums):
    total = 0
    for num in nums:
        if -100 <= num <= -55:
            total += num
    return total