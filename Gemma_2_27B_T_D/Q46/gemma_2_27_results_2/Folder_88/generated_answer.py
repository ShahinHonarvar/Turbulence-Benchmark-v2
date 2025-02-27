def gcf_three_nums(nums):
    a = nums[47]
    b = nums[10]
    c = nums[28]
    while c:
        a, b, c = (b, c, a % b)
    return a