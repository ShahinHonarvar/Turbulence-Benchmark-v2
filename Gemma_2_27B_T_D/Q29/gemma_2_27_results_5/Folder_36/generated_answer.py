def gcf_two_nums(nums):
    a = nums[429]
    b = nums[289]
    while b:
        a, b = (b, a % b)
    return a