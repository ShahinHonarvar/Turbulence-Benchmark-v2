def gcf_three_nums(nums):
    a = nums[66]
    b = nums[90]
    c = nums[27]
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf