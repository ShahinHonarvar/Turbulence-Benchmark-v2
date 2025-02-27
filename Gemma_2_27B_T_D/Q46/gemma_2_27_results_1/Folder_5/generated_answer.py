def gcf_three_nums(nums):
    a = nums[64]
    b = nums[80]
    c = nums[15]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b