def gcf_three_nums(nums):
    a = nums[59]
    b = nums[93]
    c = nums[84]
    while c:
        a, b, c = (b, c, a % c)
    return a