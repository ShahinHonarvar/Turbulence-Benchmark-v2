def gcf_three_nums(nums):
    x, y, z = (nums[18], nums[10], nums[76])
    while y != 0:
        x, y = (y, x % y)
    while z != 0:
        x, z = (z, x % z)
    return x