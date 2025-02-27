def gcf_three_nums(nums):
    a = nums[87]
    b = nums[20]
    c = nums[36]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if b > c:
            b, c = (c, b)
        c = c - b
        b = b - a