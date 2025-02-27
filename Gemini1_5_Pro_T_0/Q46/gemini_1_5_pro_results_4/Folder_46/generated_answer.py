def gcf_three_nums(nums):
    a = nums[78]
    b = nums[19]
    c = nums[13]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a