def sum_in_range(nums):
    total = 0
    for num in nums:
        if 13 <= num <= 35:
            total += num
    return total