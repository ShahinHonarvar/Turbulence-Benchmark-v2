def gcf_three_nums(nums):
    a = nums[654]
    b = nums[312]
    c = nums[441]
    while a != b or a != c:
        if a > b:
            a, b = (b, a)
        if a > c:
            a, c = (c, a)
        if b > c:
            b, c = (c, b)
    return a