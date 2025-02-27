def gcf_three_nums(nums):
    x1, x2, x3 = (nums[56], nums[54], nums[13])
    factor = x1
    while factor > 0:
        if x2 % factor == 0 and x3 % factor == 0:
            return factor
        factor -= 1
    return 1