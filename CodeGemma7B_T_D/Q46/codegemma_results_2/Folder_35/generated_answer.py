def gcf_three_nums(nums):
    a, b, c = (nums[742], nums[888], nums[629])
    if b < a:
        a, b = (b, a)
    if c < b:
        b, c = (b, c)
    if a % b == 0 and c % b == 0:
        return b
    if a % c == 0 and b % c == 0:
        return c
    g = a % b
    while g != 0:
        if c % g == 0:
            return g
        a, b, g = (b, g, b % g)