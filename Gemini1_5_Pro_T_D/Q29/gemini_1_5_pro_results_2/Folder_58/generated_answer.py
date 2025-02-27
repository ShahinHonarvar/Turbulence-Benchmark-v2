def gcf_two_nums(nums):
    a = nums[129]
    b = nums[582]
    while b:
        a, b = (b, a % b)
    return a