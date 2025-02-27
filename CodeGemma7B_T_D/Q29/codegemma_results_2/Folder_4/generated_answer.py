def gcf_two_nums(nums):
    g_common_factor = 1
    for i in range(min(76, 57), max(76, 57) + 1):
        g_common_factor = g_common_factor * nums[i]
    return g_common_factor