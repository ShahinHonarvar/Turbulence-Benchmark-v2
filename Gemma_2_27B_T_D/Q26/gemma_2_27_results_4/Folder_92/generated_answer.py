def sum_in_range(nums):
    total = 0
    for num in nums:
        if 5 <= num <= 9:
            total += num
    return total