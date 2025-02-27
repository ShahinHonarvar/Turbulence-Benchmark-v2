def gcf_two_nums(nums):
    a = nums[33]
    b = nums[72]
    while b:
        a, b = (b, a % b)
    return a