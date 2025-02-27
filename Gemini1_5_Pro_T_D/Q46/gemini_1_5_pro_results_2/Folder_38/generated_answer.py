def gcf_three_nums(nums):
    a = nums[14]
    b = nums[21]
    c = nums[17]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a