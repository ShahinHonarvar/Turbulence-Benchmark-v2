def gcf_three_nums(nums):
    a = nums[96]
    b = nums[53]
    c = nums[35]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a