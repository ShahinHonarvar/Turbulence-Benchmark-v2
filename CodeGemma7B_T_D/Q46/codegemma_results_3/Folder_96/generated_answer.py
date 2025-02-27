def gcf_three_nums(nums):
    a, b, c = (nums[29], nums[74], nums[49])
    g_common = 0
    for l in range(a, 0, -1):
        if a % l == 0 and b % l == 0 and (c % l == 0):
            g_common = l
    return g_common