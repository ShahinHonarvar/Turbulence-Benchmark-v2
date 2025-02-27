def gcf_two_nums(nums):
    a, b = (nums[20], nums[83])
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a