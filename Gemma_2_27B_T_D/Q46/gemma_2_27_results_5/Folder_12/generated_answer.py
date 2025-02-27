def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a