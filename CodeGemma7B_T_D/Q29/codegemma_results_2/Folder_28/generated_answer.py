def gcf_two_nums(nums):
    a, b = (nums[48], nums[76])
    while b:
        a, b = (b, a % b)
    return a