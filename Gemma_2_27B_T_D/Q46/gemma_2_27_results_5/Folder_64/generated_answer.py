def gcf_three_nums(nums):
    a = nums[0]
    b = nums[8]
    c = nums[3]
    while c:
        a, c = (c, a % c)
    while b:
        a, b = (b, a % b)
    return a