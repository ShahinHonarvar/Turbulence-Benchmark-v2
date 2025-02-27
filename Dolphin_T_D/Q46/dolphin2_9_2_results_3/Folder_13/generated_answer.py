def gcf_three_nums(nums):
    a = nums[991]
    b = nums[244]
    c = nums[974]
    s = min(a, b, c)
    while True:
        if a % s == 0 and b % s == 0 and (c % s == 0):
            return s
        s -= 1