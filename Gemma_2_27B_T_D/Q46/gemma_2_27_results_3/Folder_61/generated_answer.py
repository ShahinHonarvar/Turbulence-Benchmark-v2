def gcf_three_nums(nums):
    a = nums[1]
    b = nums[2]
    c = nums[7]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b