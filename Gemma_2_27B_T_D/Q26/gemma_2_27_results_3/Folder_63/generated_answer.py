def sum_in_range(nums):
    total = 0
    for num in nums:
        if 18 <= num <= 52:
            total += num
    return total