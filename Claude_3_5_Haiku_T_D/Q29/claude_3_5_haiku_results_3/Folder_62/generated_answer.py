def gcf_two_nums(nums):
    a = nums[51]
    b = nums[31]
    while b != 0:
        a, b = (b, a % b)
    return a