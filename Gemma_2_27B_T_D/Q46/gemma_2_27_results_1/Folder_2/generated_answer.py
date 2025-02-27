def gcf_three_nums(nums):
    a = nums[307]
    b = nums[920]
    c = nums[463]
    while a:
        a, b = (b % a, a)
        a, c = (c % a, a)
    return