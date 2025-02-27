def gcf_three_nums(nums):
    a = nums[19]
    b = nums[49]
    c = nums[74]
    gcf = 1
    i = 1
    while i <= min(a, b, c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf