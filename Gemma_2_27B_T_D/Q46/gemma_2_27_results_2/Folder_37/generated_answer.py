def gcf_three_nums(nums):
    a = nums[41]
    b = nums[69]
    c = nums[28]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b