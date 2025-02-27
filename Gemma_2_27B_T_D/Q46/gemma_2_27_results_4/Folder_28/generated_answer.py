def gcf_three_nums(nums):
    a = nums[99]
    b = nums[63]
    c = nums[74]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a