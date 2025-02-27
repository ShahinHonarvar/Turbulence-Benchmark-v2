def gcf_three_nums(nums):
    a = nums[76]
    b = nums[64]
    c = nums[28]
    while c:
        a, b, c = (b, c, a % c)
    return a