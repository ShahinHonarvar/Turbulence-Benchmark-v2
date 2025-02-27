def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    while c:
        a, b, c = (b, c, a % b)
    return a