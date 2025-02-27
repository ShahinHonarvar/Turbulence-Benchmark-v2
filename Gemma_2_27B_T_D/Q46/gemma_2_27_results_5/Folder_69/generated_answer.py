def gcf_three_nums(nums):
    a = nums[404]
    b = nums[834]
    c = nums[517]
    while a:
        a, b = (b % a, a)
    while b:
        b, c = (c % b, b)
    return c