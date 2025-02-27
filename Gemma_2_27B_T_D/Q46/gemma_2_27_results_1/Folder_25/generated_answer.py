def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a