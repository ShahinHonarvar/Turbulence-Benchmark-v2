def gcf_three_nums(nums):
    a = nums[96]
    b = nums[57]
    c = nums[85]
    while c:
        a, b, c = (b, c, a % b)
    return a