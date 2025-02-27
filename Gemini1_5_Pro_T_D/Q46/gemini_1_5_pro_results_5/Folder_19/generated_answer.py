def gcf_three_nums(nums):
    a = nums[40]
    b = nums[15]
    c = nums[99]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a