def gcf_two_nums(nums):
    a = nums[28]
    b = nums[17]
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a