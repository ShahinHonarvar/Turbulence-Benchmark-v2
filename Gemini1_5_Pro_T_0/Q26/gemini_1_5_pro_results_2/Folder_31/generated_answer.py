def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 60 and x <= 97:
            sum += x
    return sum