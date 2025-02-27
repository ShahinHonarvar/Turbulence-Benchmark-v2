def gcf_three_nums(nums):
    a = nums[25]
    b = nums[76]
    c = nums[57]
    while True:
        if a == b == c:
            return a
        if a < b:
            b, a = (a, b)
        if a < c:
            c, a = (a, c)
        if b < c:
            c, b = (b, c)
        a -= b
        c -= b