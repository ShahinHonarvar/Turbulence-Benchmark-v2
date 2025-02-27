def gcf_two_nums(nums):
    a, b = (nums[3], nums[8])
    while b != 0:
        a, b = (b, a % b)
    return a