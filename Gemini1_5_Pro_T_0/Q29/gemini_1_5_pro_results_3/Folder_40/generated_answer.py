def gcf_two_nums(nums):
    a = nums[7]
    b = nums[9]
    while b:
        a, b = (b, a % b)
    return a