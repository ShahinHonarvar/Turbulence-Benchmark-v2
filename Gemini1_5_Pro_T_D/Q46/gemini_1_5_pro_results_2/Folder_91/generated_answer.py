def gcf_three_nums(nums):
    a = nums[8]
    b = nums[9]
    c = nums[3]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a