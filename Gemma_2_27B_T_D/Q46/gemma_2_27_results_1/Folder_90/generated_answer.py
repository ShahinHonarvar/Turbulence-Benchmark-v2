def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]
    while c:
        a, b, c = (b, c, a % b)
    return a