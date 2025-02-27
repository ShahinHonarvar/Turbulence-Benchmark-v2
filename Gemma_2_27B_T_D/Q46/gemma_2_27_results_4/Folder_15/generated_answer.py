def gcf_three_nums(nums):
    a = nums[4]
    b = nums[0]
    c = nums[8]
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