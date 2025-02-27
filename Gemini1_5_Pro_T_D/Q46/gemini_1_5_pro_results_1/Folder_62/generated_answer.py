def gcf_three_nums(nums):
    a = nums[10]
    b = nums[55]
    c = nums[36]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a