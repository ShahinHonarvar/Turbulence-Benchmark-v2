def gcf_three_nums(nums):
    a = nums[63]
    b = nums[73]
    c = nums[11]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a