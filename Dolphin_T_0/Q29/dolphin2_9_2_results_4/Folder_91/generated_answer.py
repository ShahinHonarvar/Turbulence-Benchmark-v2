def gcf_two_nums(nums):
    a = nums[4]
    b = nums[0]
    while b != 0:
        a, b = (b, a % b)
    return a