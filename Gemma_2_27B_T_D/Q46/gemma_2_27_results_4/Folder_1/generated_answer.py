def gcf_three_nums(nums):
    a = nums[74]
    b = nums[51]
    c = nums[27]
    while True:
        if a == b and a == c:
            return a
        if a > b:
            a, b = (b, a)
        if a > c:
            a, c = (c, a)
        if b > c:
            b, c = (c, b)
        c = c - a
        b = b - a