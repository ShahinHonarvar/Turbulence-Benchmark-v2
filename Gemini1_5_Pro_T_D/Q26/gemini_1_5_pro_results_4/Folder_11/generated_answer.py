def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 11 and x <= 76:
            sum += x
    return sum