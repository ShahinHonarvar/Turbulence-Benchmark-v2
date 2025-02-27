def gcf_three_nums(nums):
    a = nums[991]
    b = nums[244]
    c = nums[974]
    while a > 0:
        a, b, c = (b % a, c % a, a)
    return c