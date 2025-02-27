def gcf_three_nums(nums):
    a = nums[99]
    b = nums[28]
    c = nums[53]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if b > c:
            b, c = (c, b)
        c = c - b
        b = b - a