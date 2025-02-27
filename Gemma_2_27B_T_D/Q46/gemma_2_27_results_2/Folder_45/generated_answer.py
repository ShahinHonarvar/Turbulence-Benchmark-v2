def gcf_three_nums(nums):
    a = nums[46]
    b = nums[84]
    c = nums[23]
    while True:
        if a == b == c:
            return a
        a_temp = min(a, b, c)
        if a_temp == a:
            b = abs(b - a)
            c = abs(c - a)
            a = a_temp
        elif a_temp == b:
            a = abs(a - b)
            c = abs(c - b)
            b = a_temp
        else:
            a = abs(a - c)
            b = abs(b - c)
            c = a_temp