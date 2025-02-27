def gcf_three_nums(nums):
    a = nums[29]
    b = nums[74]
    c = nums[49]
    i = 1
    gcf = 1
    while i <= a:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf