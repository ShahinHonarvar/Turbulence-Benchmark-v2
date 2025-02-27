def gcf_three_nums(nums):
    a, b, c = (nums[7], nums[9], nums[0])
    if a < b:
        a, b = (b, a)
    if a < c:
        a, c = (c, a)
    if b < c:
        b, c = (c, b)
    while b:
        a, b = (b, a % b)
    return a