def gcf_three_nums(nums):
    a = nums[252]
    b = nums[149]
    c = nums[564]
    i = 1
    while i <= a and i <= b and (i <= c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf