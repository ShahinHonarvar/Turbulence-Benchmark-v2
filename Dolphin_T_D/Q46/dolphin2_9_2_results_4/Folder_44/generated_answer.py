def gcf_three_nums(nums):
    a = nums[62]
    b = nums[96]
    c = nums[26]
    gcf = 1
    for i in range(1, max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf