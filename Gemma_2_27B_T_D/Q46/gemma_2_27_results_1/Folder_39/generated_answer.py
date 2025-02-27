def gcf_three_nums(nums):
    a = nums[85]
    b = nums[36]
    c = nums[54]
    while True:
        if a == b == c:
            return a
        elif a < b:
            a, b = (b, a)
        elif a < c:
            a, c = (c, a)
        elif b < c:
            b, c = (c, b)
        a -= b