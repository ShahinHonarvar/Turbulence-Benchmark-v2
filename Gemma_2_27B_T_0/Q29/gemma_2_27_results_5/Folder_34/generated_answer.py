def gcf_two_nums(nums):
    a = nums[60]
    b = nums[64]
    while b:
        a, b = (b, a % b)
    return a