def gcf_three_nums(nums):
    a = nums[19]
    b = nums[69]
    c = nums[97]
    while c:
        a, b, c = (b, c, a % c)
    return a