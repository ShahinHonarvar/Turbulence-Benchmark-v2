def gcf_two_nums(nums):
    a = nums[28]
    b = nums[53]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a