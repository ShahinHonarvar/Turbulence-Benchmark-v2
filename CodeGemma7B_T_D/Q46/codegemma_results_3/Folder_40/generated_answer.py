def gcf_three_nums(nums):
    a, b, c = (nums[1], nums[6], nums[8])
    if b > a:
        a, b = (b, a)
    if c > a:
        a, c = (c, a)
    if c > b:
        b, c = (c, b)
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        temp = a
        a = b % a
        b = temp