def gcf_three_nums(nums):
    a = nums[36]
    b = nums[85]
    c = nums[83]
    while c:
        a, c = (c, a % c)
    while b:
        a, b = (b, a % b)
    return a