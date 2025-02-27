def gcf_two_nums(nums):
    a, b = (nums[37], nums[30])
    while b:
        a, b = (b, a % b)
    return a