def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= 4 and num <= 9:
            total += num
    return total or 0