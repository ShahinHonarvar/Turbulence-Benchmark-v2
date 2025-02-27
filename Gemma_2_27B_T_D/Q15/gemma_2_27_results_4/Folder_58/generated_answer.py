def sum_odd_ints_inclusive(nums):
    s = 0
    for i in range(209, 557):
        if nums[i] % 2 != 0:
            s += nums[i]
    return s