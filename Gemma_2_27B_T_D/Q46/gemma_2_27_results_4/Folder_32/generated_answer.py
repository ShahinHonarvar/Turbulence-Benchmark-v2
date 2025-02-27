def gcf_three_nums(nums):
    a = nums[20]
    b = nums[43]
    c = nums[95]
    while c:
        a, c = (c, a % c)
    while b:
        a, b = (b, a % b)
    return a