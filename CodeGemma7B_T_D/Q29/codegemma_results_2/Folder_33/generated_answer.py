def gcf_two_nums(nums):
    a, b = (nums[166], nums[106])
    common = min(a, b)
    while common > 0:
        if a % common == 0 and b % common == 0:
            return common
        else:
            common -= 1
    return 1