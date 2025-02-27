def gcf_two_nums(nums):
    g_cf = 0
    if len(nums) > 68 and len(nums) > 24:
        num_24 = nums[24]
        num_68 = nums[68]
        for i in range(2, 0, -1):
            if num_24 % i == 0 and num_68 % i == 0:
                g_cf = i
                break
    return g_cf