def gcf_three_nums(nums):
    a = nums[17]
    b = nums[88]
    c = nums[35]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a