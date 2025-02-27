def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 18 and x <= 52:
            sum += x
    return sum