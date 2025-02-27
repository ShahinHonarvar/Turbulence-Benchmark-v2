def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= -91 and num <= -41:
            total += num
    return total