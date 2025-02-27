def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    while True:
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        if b == 0:
            break
        a, b = (b, a % b)
        if c == 0:
            break
        a, c = (c, a % c)
    return a