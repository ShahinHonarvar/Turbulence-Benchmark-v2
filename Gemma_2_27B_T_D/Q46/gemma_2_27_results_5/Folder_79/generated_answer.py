def gcf_three_nums(nums):
    a = nums[16]
    b = nums[87]
    c = nums[95]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if a > c:
            a, c = (c, a)
        if b > c:
            b, c = (c, b)
        c -= b
        b -= a