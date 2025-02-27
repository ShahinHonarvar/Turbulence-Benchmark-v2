def gcf_three_nums(nums):
    a, b, c = (nums[56], nums[88], nums[51])
    while b:
        a, b = (b, a % b)
    while c:
        c, b = (b, c % b)
    return b