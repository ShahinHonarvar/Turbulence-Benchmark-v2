def gcf_three_nums(nums):
    a = nums[76]
    b = nums[35]
    c = nums[74]
    while c:
        a, b, c = (b, c, a % b)
    return a