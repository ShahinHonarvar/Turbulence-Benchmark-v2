def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a