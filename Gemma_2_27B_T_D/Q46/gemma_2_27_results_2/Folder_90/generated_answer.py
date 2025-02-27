def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]
    while a % b != 0:
        a, b = (b, a % b)
    while b % c != 0:
        b, c = (c, b % c)
    return c