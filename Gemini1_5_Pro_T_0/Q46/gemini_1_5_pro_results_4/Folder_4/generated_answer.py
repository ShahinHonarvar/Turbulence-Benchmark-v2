def gcf_three_nums(nums):
    a = nums[24]
    b = nums[25]
    c = nums[80]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a