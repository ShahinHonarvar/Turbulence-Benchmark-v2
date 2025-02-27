def gcf_two_nums(nums):
    if nums[380] == 0 and nums[327] == 0:
        return 0
    a = nums[380]
    b = nums[327]
    while b != 0:
        a, b = (b, a % b)
    return a