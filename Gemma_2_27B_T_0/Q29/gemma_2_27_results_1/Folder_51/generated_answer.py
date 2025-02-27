def gcf_two_nums(nums):
    a = nums[46]
    b = nums[84]
    while b:
        a, b = (b, a % b)
    return a