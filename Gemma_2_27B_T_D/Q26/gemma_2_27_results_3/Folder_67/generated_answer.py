def sum_in_range(nums):
    total = 0
    for num in nums:
        if 31 <= num <= 50:
            total += num
    return total