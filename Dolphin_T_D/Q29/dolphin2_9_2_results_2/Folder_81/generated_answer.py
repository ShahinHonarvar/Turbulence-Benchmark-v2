def gcf_two_nums(nums):
    a = nums[20]
    b = nums[83]
    while b != 0:
        r = a % b
        a = b
        b = r
    return a