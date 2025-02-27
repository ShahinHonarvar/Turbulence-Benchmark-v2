def gcf_three_nums(nums):
    a = nums[637]
    b = nums[411]
    c = nums[757]
    while c:
        a, b, c = (b, c, a % c)
    return a