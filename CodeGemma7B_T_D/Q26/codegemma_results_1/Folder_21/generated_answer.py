def sum_in_range(nums):
    summ = 0
    for n in nums:
        if n >= 138 and n <= 858:
            summ += n
    return summ or 0