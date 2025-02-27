def sum_odd_ints_inclusive(nums):
    res = 0
    for i in range(4):
        if i >= 0 and i <= 3 and (i % 2 != 0):
            res += nums[i]
    return res