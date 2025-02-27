def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
    while True:
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        if b == 0:
            return c
        if c == 0:
            return b
        a = a - b
        c = c - b