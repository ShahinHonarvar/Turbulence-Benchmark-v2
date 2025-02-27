def gcf_three_nums(nums):
    a = nums[7]
    b = nums[9]
    c = nums[0]
    gcf = int(a)
    while a > 1 or b != 0 or c != 0:
        if b == 0:
            a, c = (c, a)
        elif c == 0:
            a, b = (b, a)
        else:
            a, b, c = (b, c, a % b)
        gcf = int(gcf * a * b * c / (b * c + a))
    return gcf