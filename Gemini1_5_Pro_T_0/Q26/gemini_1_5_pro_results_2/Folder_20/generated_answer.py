def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= -64 and x <= 42:
            sum += x
    return sum