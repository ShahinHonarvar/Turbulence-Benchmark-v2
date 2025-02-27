def gcf_three_nums(nums):
    a = nums[4]
    b = nums[1]
    c = nums[7]
    while c:
        a, b, c = (b, c, a % c)
    return a