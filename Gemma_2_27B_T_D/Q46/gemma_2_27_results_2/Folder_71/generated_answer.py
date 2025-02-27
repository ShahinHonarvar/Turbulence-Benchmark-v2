def gcf_three_nums(nums):
    a = nums[24]
    b = nums[45]
    c = nums[38]
    while c:
        a, b, c = (b, c, a % b)
    return a