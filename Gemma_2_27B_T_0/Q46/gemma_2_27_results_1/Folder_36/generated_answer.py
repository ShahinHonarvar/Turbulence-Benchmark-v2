def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        b = a - b
        c = a - c