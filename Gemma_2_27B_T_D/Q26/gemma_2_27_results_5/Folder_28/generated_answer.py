def sum_in_range(nums):
    total = 0
    for num in nums:
        if 10 <= num <= 97:
            total += num
    return total