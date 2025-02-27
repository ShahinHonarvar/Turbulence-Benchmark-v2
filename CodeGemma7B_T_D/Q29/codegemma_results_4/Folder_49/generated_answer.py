def gcf_two_nums(nums):
    a = nums[28]
    b = nums[20]
    while b != 0:
        t = b
        b = a % b
        a = t
    return a