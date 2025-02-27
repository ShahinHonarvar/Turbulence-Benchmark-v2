def gcf_two_nums(nums):
    a = nums[15]
    b = nums[99]
    while b:
        a, b = (b, a % b)
    return a