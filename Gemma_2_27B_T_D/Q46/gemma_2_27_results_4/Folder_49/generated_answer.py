def gcf_three_nums(nums):
    a = nums[34]
    b = nums[38]
    c = nums[77]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if b > c:
            b, c = (c, b)
        c = c - b
        b = b - a