def gcf_three_nums(nums):
    a = nums[47]
    b = nums[10]
    c = nums[28]
    while True:
        if a == b == c:
            return a
        if a < b:
            b, a = (a, b)
        if a < c:
            c, a = (a, c)
        a -= b
        c -= b