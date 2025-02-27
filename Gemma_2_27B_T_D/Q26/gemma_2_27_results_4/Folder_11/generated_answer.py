def sum_in_range(nums):
    total = 0
    for num in nums:
        if 11 <= num <= 76:
            total += num
    return total