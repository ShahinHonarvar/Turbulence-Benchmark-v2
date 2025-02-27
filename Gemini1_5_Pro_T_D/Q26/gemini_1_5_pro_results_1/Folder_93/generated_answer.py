def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= -23 and x <= 64:
            sum += x
    return sum