def gcf_three_nums(nums):
    a, b, c = (nums[96], nums[57], nums[85])
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a