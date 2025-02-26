def gcf_two_nums(nums):
    a, b = (nums[13], nums[66])
    while b:
        a, b = (b, a % b)
    return a