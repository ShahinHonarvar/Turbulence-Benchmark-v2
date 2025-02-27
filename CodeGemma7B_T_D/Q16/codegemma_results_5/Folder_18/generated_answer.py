def sum_even_ints_inclusive(nums):
    summ = 0
    lo, hi = (35, 49)
    for i in range(lo, hi + 1):
        if i % 2 == 0:
            summ += nums[i]
    return summ or 0