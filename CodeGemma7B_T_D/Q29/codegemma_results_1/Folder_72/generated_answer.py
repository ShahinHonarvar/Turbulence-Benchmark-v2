def gcf_two_nums(nums):
    a, b = (nums[18], nums[37])
    while b:
        a, b = (b, a % b)
    return a