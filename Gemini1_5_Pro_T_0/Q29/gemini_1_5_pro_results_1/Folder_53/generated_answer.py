def gcf_two_nums(nums):
    a = nums[28]
    b = nums[67]
    while b:
        a, b = (b, a % b)
    return a