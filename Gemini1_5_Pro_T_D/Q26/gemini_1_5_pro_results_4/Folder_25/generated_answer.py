def sum_in_range(nums):
    sum = 0
    for x in nums:
        if -10 <= x <= 48:
            sum += x
    return sum