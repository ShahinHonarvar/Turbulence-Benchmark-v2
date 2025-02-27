def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= 782 and num <= 787:
            total += num
    return total or 0