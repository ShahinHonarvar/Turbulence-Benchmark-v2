def gcf_three_nums(nums):
    a = nums[53]
    b = nums[23]
    c = nums[45]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a