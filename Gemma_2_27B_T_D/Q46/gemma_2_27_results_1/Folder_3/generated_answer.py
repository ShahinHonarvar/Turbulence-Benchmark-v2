def gcf_three_nums(nums):
    a = nums[31]
    b = nums[69]
    c = nums[40]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if b < c:
            b, c = (c, b)
        c = c - b
    b = b - c