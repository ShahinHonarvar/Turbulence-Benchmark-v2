def gcf_three_nums(nums):
    a = nums[4]
    b = nums[1]
    c = nums[7]
    if a < b:
        a, b = (b, a)
    for i in range(b, 1, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1