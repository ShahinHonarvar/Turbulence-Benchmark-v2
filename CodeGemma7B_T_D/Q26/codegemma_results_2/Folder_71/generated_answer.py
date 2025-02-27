def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= 39 and num <= 43:
            total += num
    return total or 0