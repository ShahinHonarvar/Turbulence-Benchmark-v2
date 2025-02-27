def gcf_three_nums(nums):
    a = nums[25]
    b = nums[76]
    c = nums[57]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a