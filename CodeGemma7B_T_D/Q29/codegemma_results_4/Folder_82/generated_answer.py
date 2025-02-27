def gcf_two_nums(nums):
    a, b = (nums[33], nums[72])
    while b:
        a, b = (b, a % b)
    return a