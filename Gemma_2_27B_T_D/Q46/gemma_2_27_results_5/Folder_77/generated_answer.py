def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        b = a - b
        c = a - c