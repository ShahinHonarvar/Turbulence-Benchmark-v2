def gcf_two_nums(nums):
    a, b = (nums[21], nums[17])
    while b:
        a, b = (b, a % b)
    return a