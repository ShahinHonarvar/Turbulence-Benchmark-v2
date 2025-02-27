def sum_in_range(nums):
    total = 0
    for num in range(2, 7):
        if num in nums:
            total += num
    return total