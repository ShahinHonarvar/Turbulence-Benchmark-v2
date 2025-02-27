def sum_in_range(nums):
    sum = 0
    for x in nums:
        if 4 <= x <= 8:
            sum += x
    return sum