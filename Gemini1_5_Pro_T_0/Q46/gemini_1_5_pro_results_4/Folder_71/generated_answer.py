def gcf_three_nums(nums):
    a = nums[24]
    b = nums[45]
    c = nums[38]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a