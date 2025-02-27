def sum_in_range(nums):
    total = 0
    for num in nums:
        if num in range(139, 768):
            total += num
    return total