def gcf_two_nums(nums):
    a = nums[372]
    b = nums[752]
    while b:
        a, b = (b, a % b)
    return a