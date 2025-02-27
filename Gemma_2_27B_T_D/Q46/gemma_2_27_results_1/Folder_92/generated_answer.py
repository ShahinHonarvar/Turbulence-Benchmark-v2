def gcf_three_nums(nums):
    a = nums[7]
    b = nums[9]
    c = nums[0]
    while True:
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        if b < c:
            b, c = (c, b)
        if a == b == c:
            return a
        if a == b:
            return a
        if a == c:
            return a
        if b == c:
            return b
        a -= b
        c -= b