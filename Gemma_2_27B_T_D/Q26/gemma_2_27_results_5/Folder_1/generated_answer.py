def sum_in_range(nums):
    total = 0
    for num in nums:
        if -97 <= num <= -48:
            total += num
    return total