def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    i = 1
    while i <= a and i <= b and (i <= c):
        if a % i == b % i == c % i == 0:
            gcf = i
        else:
            gcf = 1
        i += 1
    return gcf