def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
    return c