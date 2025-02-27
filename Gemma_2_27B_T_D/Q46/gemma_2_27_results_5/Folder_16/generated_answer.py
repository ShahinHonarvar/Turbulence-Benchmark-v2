def gcf_three_nums(nums):
    a = nums[558]
    b = nums[110]
    c = nums[628]
    while c:
        a, b, c = (b, c, a % c)
    return a