def gcf_three_nums(nums):
    a = nums[38]
    b = nums[52]
    c = nums[69]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a