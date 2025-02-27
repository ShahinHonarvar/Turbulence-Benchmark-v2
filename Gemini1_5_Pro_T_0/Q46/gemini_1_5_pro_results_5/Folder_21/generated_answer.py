def gcf_three_nums(nums):
    a = nums[412]
    b = nums[932]
    c = nums[337]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a