def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= 90 and num <= 97:
            total += num
    return total or 0