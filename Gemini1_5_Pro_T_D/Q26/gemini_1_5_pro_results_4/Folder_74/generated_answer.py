def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 13 and x <= 35:
            sum += x
    return sum