def gcf_three_nums(nums):
    a = nums[22]
    b = nums[97]
    c = nums[64]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a