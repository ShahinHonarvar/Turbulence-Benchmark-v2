def gcf_three_nums(nums):
    a, b, c = (nums[13], nums[70], nums[32])
    g_f = a
    while g_f > 0:
        if b % g_f == 0 and c % g_f == 0:
            return g_f
        g_f -= 1