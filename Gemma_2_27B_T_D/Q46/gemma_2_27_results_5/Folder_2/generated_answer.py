def gcf_three_nums(nums):
    a = nums[307]
    b = nums[920]
    c = nums[463]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a