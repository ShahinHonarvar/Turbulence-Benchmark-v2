def gcf_two_nums(nums):
    a = nums[64]
    b = nums[80]
    while b:
        a, b = (b, a % b)
    return a