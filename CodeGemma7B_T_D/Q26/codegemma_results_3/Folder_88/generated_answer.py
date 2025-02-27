def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= 1 and num <= 7:
            total += num
    return total