def gcf_three_nums(nums):
    a = nums[67]
    b = nums[84]
    c = nums[13]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b