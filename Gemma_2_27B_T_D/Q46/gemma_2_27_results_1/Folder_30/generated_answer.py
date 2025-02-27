def gcf_three_nums(nums):
    a = nums[76]
    b = nums[35]
    c = nums[74]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if a > c:
            a, c = (c, a)
        if b > c:
            b, c = (c, b)
        c -= a
        b -= a