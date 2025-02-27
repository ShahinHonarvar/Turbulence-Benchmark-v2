def gcf_three_nums(nums):
    a = nums[27]
    b = nums[85]
    c = nums[51]
    while b != c:
        if b > c:
            b -= c
        else:
            c -= b
    return b