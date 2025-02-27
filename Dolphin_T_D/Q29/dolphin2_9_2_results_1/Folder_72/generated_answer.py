def gcf_two_nums(nums):
    a = nums[18]
    b = nums[37]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a