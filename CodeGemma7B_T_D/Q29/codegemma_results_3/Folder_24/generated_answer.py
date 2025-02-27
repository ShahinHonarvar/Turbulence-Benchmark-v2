def gcf_two_nums(nums):
    a = nums[84]
    b = nums[21]
    while b != 0:
        a, b = (b, a % b)
    return a