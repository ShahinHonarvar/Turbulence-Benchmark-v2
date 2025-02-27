def gcf_three_nums(nums):
    a = nums[90]
    b = nums[84]
    c = nums[47]
    while a:
        a, b = (b % a, a)
    while c:
        c, b = (b % c, c)
    return b