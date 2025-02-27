def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    while c:
        a, c = (c, a % c)
    while b:
        a, b = (b, a % b)
    return a