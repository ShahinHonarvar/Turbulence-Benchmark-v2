def gcf_three_nums(nums):
    a = nums[24]
    b = nums[25]
    c = nums[80]
    while c:
        a, b, c = (b, c, a % b)
    return a