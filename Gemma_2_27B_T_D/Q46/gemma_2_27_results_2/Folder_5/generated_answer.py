def gcf_three_nums(nums):
    a = nums[64]
    b = nums[80]
    c = nums[15]
    while c:
        a, b = (b, a % b)
        a, c = (c, a % c)
    return a