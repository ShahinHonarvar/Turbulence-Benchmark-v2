def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a