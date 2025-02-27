def gcf_two_nums(nums):
    a = nums[91]
    b = nums[45]
    while b:
        a, b = (b, a % b)
    return a