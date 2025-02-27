def gcf_two_nums(nums):
    a, b = (nums[29], nums[74])
    while b:
        a, b = (b, a % b)
    return a