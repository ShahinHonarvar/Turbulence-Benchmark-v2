def gcf_three_nums(nums):
    a, b, c = (nums[19], nums[94], nums[78])
    while c:
        a, b, c = (b % c, c, b % c)
    return a