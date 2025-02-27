def gcf_three_nums(nums):
    a = nums[99]
    b = nums[95]
    c = nums[80]
    while c:
        a, b, c = (b, c, a % c)
    return a