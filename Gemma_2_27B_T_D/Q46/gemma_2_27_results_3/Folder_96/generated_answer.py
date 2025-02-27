def gcf_three_nums(nums):
    a = nums[29]
    b = nums[74]
    c = nums[49]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a