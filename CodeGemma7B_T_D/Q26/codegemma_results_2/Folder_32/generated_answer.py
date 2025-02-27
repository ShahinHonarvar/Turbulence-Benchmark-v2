def sum_in_range(nums):
    total = 0
    for num in nums:
        if num in range(-358, 186):
            total += num
    return total