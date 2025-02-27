def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 3 and x <= 9:
            sum += x
    return sum