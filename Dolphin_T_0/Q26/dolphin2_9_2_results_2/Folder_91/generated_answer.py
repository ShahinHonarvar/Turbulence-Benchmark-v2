def sum_in_range(nums):
    total = 0
    for num in nums:
        if -8 <= num <= 8:
            total += num
    return total