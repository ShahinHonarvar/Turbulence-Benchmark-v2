def gcf_two_nums(nums):
    a = nums[66]
    b = nums[90]
    while b:
        a, b = (b, a % b)
    return a