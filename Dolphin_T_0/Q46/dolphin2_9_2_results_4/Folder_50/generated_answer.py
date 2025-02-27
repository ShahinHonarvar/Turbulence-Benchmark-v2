def gcf_three_nums(nums):
    a = nums[20]
    b = nums[35]
    c = nums[74]
    gcf = a
    i = 1
    while i <= min(b, c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf