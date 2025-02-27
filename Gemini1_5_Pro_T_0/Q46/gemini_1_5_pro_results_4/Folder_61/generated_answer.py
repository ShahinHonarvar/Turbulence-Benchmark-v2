def gcf_three_nums(nums):
    a = nums[1]
    b = nums[2]
    c = nums[7]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a