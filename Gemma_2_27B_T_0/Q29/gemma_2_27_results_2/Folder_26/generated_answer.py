def gcf_two_nums(nums):
    a = nums[49]
    b = nums[31]
    while b:
        a, b = (b, a % b)
    return a