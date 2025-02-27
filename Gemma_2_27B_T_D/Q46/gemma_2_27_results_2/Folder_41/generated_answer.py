def gcf_three_nums(nums):
    a = nums[19]
    b = nums[94]
    c = nums[78]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        if a < c:
            a, c = (c, a)
        c -= a