def gcf_three_nums(nums):
    a = nums[99]
    b = nums[95]
    c = nums[80]
    while a:
        a, b, c = (b % a, c % a, a)
    return c