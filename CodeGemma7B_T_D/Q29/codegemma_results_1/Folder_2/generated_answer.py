def gcf_two_nums(nums):
    a = nums[372]
    b = nums[752]
    while b != 0:
        a, b = (b, a % b)
    return a