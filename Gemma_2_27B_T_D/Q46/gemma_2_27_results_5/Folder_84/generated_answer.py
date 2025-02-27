def gcf_three_nums(nums):
    a = nums[695]
    b = nums[710]
    c = nums[914]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b