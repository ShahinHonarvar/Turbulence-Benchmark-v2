def gcf_two_nums(nums):
    a = nums[84]
    b = nums[13]
    while b:
        a, b = (b, a % b)
    return a