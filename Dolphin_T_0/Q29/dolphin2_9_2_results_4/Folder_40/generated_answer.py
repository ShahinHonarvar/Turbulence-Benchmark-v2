def gcf_two_nums(nums):
    a = nums[7]
    b = nums[9]
    gcfd = a
    while b != 0:
        if a > b:
            a = rem(a, b)
        else:
            b = rem(b, a)
        gcfd = a
    return gcfd