def gcf_three_nums(nums):
    a = nums[16]
    b = nums[87]
    c = nums[95]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a