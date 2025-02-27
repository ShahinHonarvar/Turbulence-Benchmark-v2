def gcf_two_nums(nums):
    a = nums[96]
    b = nums[32]
    while b:
        a, b = (b, a % b)
    return a