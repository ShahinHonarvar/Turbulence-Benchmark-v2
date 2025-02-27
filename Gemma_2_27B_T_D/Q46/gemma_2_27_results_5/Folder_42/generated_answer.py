def gcf_three_nums(nums):
    a = nums[19]
    b = nums[69]
    c = nums[97]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a