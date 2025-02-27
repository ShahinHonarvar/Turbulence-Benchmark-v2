def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 38 and x <= 81:
            sum += x
    return sum