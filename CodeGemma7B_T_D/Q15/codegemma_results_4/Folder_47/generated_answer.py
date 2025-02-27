def sum_odd_ints_inclusive(nums):
    res = 0
    i = 37
    while i <= 76:
        if i >= 37 and i <= 76 and (nums[i] % 2 != 0):
            res += nums[i]
        i += 1
    return res