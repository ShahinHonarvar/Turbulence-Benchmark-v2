def gcf_three_nums(nums):
    a = nums[654]
    b = nums[312]
    c = nums[441]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a = a - b
        c = c - b