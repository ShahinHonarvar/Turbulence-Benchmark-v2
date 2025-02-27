def gcf_two_nums(nums):
    a = nums[63]
    b = nums[84]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a