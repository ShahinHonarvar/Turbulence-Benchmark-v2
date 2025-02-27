def sum_odd_ints_inclusive(nums):
    s = 0
    for i in range(262, 747, 2):
        s += nums[i]
    return 0 if s == 0 else s