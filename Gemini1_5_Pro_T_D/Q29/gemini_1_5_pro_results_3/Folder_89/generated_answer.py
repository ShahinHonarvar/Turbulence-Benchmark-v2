def gcf_two_nums(nums):
    a = nums[37]
    b = nums[30]
    while b:
        a, b = (b, a % b)
    return a