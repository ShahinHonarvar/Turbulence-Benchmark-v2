def gcf_three_nums(nums):
    a = nums[44]
    b = nums[91]
    c = nums[42]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a