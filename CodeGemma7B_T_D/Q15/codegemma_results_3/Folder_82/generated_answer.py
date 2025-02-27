def sum_odd_ints_inclusive(nums):
    s = 0
    for i in range(20, 201):
        if nums[i] % 2 != 0:
            s += nums[i]
    if s == 0:
        return 0
    else:
        return s