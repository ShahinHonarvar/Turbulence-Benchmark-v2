def gcf_three_nums(nums):
    a = nums[78]
    b = nums[19]
    c = nums[13]
    while True:
        if a == b == c:
            return a
        if a >= b and a >= c:
            a = a - b if b < c else a - c
        elif b >= a and b >= c:
            b = b - a if a < c else b - c
        else:
            c = c - a if a < b else c - b