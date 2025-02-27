def gcf_two_nums(nums):
    a = nums[380]
    b = nums[327]
    while b != 0:
        a, b = (b, a % b)
    return a