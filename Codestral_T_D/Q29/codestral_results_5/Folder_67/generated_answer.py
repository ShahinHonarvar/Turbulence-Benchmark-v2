def gcf_two_nums(nums):
    a = nums[64]
    b = nums[28]
    while b != 0:
        a, b = (b, a % b)
    return a