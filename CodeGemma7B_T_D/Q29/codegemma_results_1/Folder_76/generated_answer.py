def gcf_two_nums(nums):
    a, b = (nums[184], nums[307])
    a, b = (b, a % b)
    return a