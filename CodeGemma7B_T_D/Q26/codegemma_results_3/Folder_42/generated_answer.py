def sum_in_range(nums):
    total = 0
    for num in nums:
        if 141 <= num <= 262:
            total += num
    if total == 0:
        total = None
    return total