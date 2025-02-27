def gcf_three_nums(nums):
    a = nums[59]
    b = nums[93]
    c = nums[84]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a