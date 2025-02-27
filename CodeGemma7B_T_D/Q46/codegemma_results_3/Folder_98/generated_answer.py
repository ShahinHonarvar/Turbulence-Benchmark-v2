def gcf_three_nums(nums):
    a, b, c = (nums[8], nums[2], nums[1])
    x, y = (a, b)
    gcd = a if a < b else b
    while True:
        if x == y:
            return gcd
        elif x > y:
            x = x - y
        else:
            y = y - x