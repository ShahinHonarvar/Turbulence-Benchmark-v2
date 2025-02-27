def sum_in_range(nums):
    total = 0
    for num in nums:
        if 36 <= num <= 52:
            total += num
    if total == 0:
        return 0
    return total