def gcf_three_nums(nums):
    a = nums[66]
    b = nums[83]
    c = nums[12]
    while b != 0:
        a, b = (b, a % b)
    return a