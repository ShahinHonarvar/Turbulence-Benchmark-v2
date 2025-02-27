def sum_in_range(nums):
    sum_range = 0
    for n in nums:
        if n >= 18 and n <= 52:
            sum_range += n
    return sum_range