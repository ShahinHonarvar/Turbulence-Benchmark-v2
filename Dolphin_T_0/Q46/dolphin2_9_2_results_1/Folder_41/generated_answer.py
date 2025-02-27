def gcf_three_nums(nums):
    a = nums[19]
    b = nums[94]
    c = nums[78]
    g_cd_ab = 0
    while b != 0:
        if b < a:
            a, b = (b, a)
        g_cd_ab = a % b
        a = b
        b = g_cd_ab
    gcd_abc = g_cd_ab
    while c != 0:
        if c < gcd_abc:
            gcd_abc, c = (c, gcd_abc)
        g_cd_ab = gcd_abc % c
        gcd_abc = c
        c = g_cd_ab
    return gcd_abc