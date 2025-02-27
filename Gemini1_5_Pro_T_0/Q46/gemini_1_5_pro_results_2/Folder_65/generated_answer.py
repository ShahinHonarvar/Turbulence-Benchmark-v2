def gcf_three_nums(nums):
    a = nums[18]
    b = nums[10]
    c = nums[76]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a