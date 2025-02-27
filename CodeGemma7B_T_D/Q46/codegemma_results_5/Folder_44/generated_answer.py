def gcf_three_nums(nums):
    a = nums[62]
    b = nums[96]
    c = nums[26]
    if b > a:
        a, b = (b, a)
    if c > b:
        b, c = (c, b)
    while b != 0:
        a, b = (b, a % b)
    return a