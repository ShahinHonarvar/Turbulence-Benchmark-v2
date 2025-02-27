def gcf_three_nums(nums):
    a = nums[876]
    b = nums[203]
    c = nums[100]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if b > c:
            b, c = (c, b)
        c = c - b
        b = b - a