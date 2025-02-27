def sum_in_range(nums):
    sum = 0
    for x in nums:
        if -3 <= x <= 6:
            sum += x
    return sum