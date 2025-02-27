def gcf_three_nums(nums):
    a = nums[742]
    b = nums[888]
    c = nums[629]
    while True:
        if a == b == c:
            return a
        if a >= b:
            a = a - b
        if b >= c:
            b = b - c
        if c >= a:
            c = c - a