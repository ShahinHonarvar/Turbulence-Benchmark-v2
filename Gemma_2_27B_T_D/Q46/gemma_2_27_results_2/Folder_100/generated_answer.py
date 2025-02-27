def gcf_three_nums(nums):
    a = nums[21]
    b = nums[51]
    c = nums[33]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        a -= c
        b -= c