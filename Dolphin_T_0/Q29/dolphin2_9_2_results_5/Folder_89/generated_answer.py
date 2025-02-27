def gcf_two_nums(nums):
    a = nums[37]
    b = nums[30]
    if a > b:
        a, b = (b, a)
    while b % a != 0:
        a = b % a
        b = a
    return a