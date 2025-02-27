def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    while True:
        if a < b:
            a, b = (b, a)
        if b < c:
            b, c = (c, b)
        if a < c:
            a, c = (c, a)
        if a == b == c:
            return a
        if a == b:
            return a
        if a == c:
            return a
        if b == c:
            return b
        a -= c
        b -= c