def gcf_two_nums(nums):
    a = nums[8]
    b = nums[9]
    while b != 0:
        a, b = (b, a % b)
    return a