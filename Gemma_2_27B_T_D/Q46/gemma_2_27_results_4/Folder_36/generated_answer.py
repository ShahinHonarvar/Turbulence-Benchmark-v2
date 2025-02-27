def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    while a:
        a, b, c = (b % a, c % a, a)
    return c