def gcf_three_nums(nums):
    a = nums[74]
    b = nums[60]
    c = nums[28]
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf