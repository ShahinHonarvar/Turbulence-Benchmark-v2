def gcf_three_nums(nums):
    a = nums[49]
    b = nums[46]
    c = nums[13]
    while True:
        if a == b == c:
            return a
        if a > b:
            if a > c:
                a = a - c
            else:
                a = a - b
        elif b > c:
            b = b - c
        else:
            b = b - a