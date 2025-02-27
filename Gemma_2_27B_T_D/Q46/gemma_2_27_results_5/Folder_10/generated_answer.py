def gcf_three_nums(nums):
    a = nums[86]
    b = nums[89]
    c = nums[49]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a