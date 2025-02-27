def gcf_three_nums(nums):
    a = nums[4]
    b = nums[1]
    c = nums[7]
    while c:
        a, c = (c, a % c)
    while b:
        a, b = (b, a % b)
    return a