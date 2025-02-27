def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
    while c:
        a, b, c = (b, c, a % b)
    return a