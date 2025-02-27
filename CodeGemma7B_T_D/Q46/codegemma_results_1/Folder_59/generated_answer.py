def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    while b and c:
        if b < c:
            a, b = (b, a % b)
        else:
            a, c = (c, a % c)
    return a