def gcf_two_nums(nums):
    a = nums[83]
    b = nums[14]
    while b != 0:
        a, b = (b, a % b)
    return a