def gcf_three_nums(nums):
    a = nums[66]
    b = nums[90]
    c = nums[27]
    while c:
        a, b, c = (b, c, a % c)
    return a