def gcf_three_nums(nums):
    a = nums[74]
    b = nums[51]
    c = nums[27]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if b > c:
            b, c = (c, b)
        c -= b
        b -= a