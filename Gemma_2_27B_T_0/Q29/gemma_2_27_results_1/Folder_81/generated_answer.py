def gcf_two_nums(nums):
    a = nums[20]
    b = nums[83]
    while b:
        a, b = (b, a % b)
    return a