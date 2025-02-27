def gcf_three_nums(nums):
    a = nums[10]
    b = nums[55]
    c = nums[36]
    i = 1
    while i <= a and i <= b and (i <= c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
            i += 1
    return gcf