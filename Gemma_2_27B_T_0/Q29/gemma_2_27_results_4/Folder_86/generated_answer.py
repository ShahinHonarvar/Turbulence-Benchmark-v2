def gcf_two_nums(nums):
    a = nums[793]
    b = nums[449]
    while b:
        a, b = (b, a % b)
    return a