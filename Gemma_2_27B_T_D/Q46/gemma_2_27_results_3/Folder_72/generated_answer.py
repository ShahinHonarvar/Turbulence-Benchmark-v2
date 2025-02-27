def gcf_three_nums(nums):
    a = nums[44]
    b = nums[91]
    c = nums[42]
    while a != b or a != c:
        if a > b:
            a, b = (b, a)
        if a > c:
            a, c = (c, a)
        b = b - a
        c = c - a
    return a