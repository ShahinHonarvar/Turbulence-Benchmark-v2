def gcf_two_nums(nums):
    a = nums[13]
    b = nums[66]
    while b:
        a, b = (b, a % b)
    return a