def gcf_three_nums(nums):
    a = nums[90]
    b = nums[54]
    c = nums[96]
    while c:
        a, b, c = (b, c, a % c)
    return a