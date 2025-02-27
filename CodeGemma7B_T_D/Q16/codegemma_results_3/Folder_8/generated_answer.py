def sum_even_ints_inclusive(nums):
    summ = 0
    for i in range(23, 24):
        if nums[i] % 2 == 0:
            summ += nums[i]
    if summ == 0:
        return 0
    return summ