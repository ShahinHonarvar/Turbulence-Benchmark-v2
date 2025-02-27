def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]
    while c:
        a, c = (c, a % c)
        b, c = (c, b % c)
    return a