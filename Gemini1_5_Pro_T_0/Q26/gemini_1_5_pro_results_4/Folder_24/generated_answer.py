def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= -91 and x <= -41:
            sum += x
    return sum