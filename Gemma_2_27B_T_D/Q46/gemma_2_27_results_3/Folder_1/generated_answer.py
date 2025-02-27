def gcf_three_nums(nums):
    a = nums[74]
    b = nums[51]
    c = nums[27]
    while c:
        a, b, c = (b, c, a % c)
    return a