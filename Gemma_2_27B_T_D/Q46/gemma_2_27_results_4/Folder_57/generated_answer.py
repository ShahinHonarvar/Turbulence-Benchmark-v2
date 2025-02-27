def gcf_three_nums(nums):
    a = nums[90]
    b = nums[41]
    c = nums[95]
    while c:
        a, b, c = (b, c, a % c)
    return a