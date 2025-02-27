def gcf_three_nums(nums):
    a, b, c = (nums[78], nums[19], nums[13])
    while b:
        a, b = (b, a % b)
    if c:
        a = a % c
    return a