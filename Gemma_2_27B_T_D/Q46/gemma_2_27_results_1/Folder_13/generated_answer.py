def gcf_three_nums(nums):
    a = nums[991]
    b = nums[244]
    c = nums[974]
    while c:
        a, b, c = (b, c, a % c)
    return a