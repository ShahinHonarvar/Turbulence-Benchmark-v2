def gcf_three_nums(nums):
    a = nums[62]
    b = nums[96]
    c = nums[26]
    while True:
        if a == b == c:
            return a
        if a < b:
            a, b = (b, a)
        if a < c:
            a, c = (c, a)
        b = a - b
        c = a - c