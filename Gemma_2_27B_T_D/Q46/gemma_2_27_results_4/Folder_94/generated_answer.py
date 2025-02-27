def gcf_three_nums(nums):
    a = nums[56]
    b = nums[88]
    c = nums[51]
    while True:
        if a == b == c:
            return a
        if a < b:
            b -= a
        elif b < a:
            a -= b
        if a < c:
            c -= a
        elif c < a:
            a -= c