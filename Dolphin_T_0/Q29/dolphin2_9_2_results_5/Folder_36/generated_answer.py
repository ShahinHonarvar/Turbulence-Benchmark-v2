def gcf_two_nums(nums):
    a = nums[429]
    b = nums[289]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a