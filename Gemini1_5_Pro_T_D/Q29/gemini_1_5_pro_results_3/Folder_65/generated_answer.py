def gcf_two_nums(nums):
    a = nums[29]
    b = nums[53]
    while b:
        a, b = (b, a % b)
    return a