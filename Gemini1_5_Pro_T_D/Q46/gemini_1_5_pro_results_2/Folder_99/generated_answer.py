def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a