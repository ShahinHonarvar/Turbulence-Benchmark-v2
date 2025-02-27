def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    if a == 1:
        return 1
    d = c
    while d != 0:
        d, c = (c % d, d)
    return a * d