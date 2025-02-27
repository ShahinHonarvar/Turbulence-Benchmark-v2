def gcf_three_nums(nums):
    a = nums[38]
    b = nums[52]
    c = nums[69]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        if b < c:
            b, c = (c, b)
        a -= b
        c -= b