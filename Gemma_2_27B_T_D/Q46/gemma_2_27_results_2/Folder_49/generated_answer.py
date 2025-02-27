def gcf_three_nums(nums):
    a = nums[34]
    b = nums[38]
    c = nums[77]
    while c:
        a, b, c = (b, c, a % b)
    return a