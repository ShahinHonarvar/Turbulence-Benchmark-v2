def sum_in_range(nums):
    total = 0
    for num in nums:
        if num >= -97 and num <= -48:
            total += num
    return total