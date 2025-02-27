def gcf_three_nums(nums):
    a = nums[944]
    b = nums[814]
    c = nums[865]
    while True:
        if a == b == c:
            return a
        if a > b:
            a, b = (b, a)
        if b > c:
            b, c = (c, b)
        c = c - b
        b = b - a