def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b