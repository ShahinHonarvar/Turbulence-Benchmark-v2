def gcf_three_nums(nums):
    a = nums[9]
    b = nums[6]
    c = nums[2]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a