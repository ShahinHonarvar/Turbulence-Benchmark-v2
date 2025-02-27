def gcf_two_nums(nums):
    a = nums[48]
    b = nums[74]
    while b:
        a, b = (b, a % b)
    return a