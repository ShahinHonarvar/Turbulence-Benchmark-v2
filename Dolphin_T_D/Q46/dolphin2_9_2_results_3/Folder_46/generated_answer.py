def gcf_three_nums(nums):
    a, b, c = (nums[78], nums[19], nums[13])
    if a < b:
        a, b = (b, a)
    if b < c:
        b, c = (c, b)
    if a < b:
        a, b = (b, a)
    while b > 0:
        a %= b
        b, a = (a, b)
    return a