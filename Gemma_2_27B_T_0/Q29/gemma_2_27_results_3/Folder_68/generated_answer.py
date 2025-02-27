def gcf_two_nums(nums):
    a = nums[8]
    b = nums[9]
    while b:
        a, b = (b, a % b)
    return a