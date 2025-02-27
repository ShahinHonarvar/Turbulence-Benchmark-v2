def sum_odd_ints_inclusive(nums):
    res, succ = (0, False)
    for i in range(25, 88):
        if nums[i] % 2 != 0:
            succ = True
            res += nums[i]
    return res * int(succ)