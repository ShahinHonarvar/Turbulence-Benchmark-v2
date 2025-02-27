def gcf_two_nums(nums):
    if nums[84] == 0 and nums[13] == 0:
        return 0
    a = nums[84]
    b = nums[13]
    while b != 0:
        a, b = (b, a % b)
    return a