def gcf_three_nums(nums):
    a = nums[18]
    b = nums[37]
    c = nums[43]
    i = 1
    while i <= min(a, b, c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            result = i
        i += 1
    return result