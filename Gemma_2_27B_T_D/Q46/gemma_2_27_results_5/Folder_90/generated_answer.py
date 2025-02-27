def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        c -= b