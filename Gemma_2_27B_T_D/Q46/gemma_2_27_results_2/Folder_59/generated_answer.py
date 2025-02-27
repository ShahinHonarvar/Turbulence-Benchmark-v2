def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    while c:
        a, b, c = (b, c, a % c)
    return a