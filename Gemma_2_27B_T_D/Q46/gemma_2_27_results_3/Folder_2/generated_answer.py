def gcf_three_nums(nums):
    a = nums[307]
    b = nums[920]
    c = nums[463]
    while a > 0:
        a, b, c = (b % a, a, c % a)
    return c