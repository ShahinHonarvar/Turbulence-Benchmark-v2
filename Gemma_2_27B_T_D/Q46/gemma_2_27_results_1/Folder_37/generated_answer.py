def gcf_three_nums(nums):
    a = nums[41]
    b = nums[69]
    c = nums[28]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a