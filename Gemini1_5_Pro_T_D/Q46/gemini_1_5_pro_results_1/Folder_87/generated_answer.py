def gcf_three_nums(nums):
    a = nums[74]
    b = nums[60]
    c = nums[28]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a