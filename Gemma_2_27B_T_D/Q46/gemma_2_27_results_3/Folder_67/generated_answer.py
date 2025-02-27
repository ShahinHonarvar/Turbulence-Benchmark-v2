def gcf_three_nums(nums):
    a = nums[70]
    b = nums[41]
    c = nums[20]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        a -= b
        b -= c