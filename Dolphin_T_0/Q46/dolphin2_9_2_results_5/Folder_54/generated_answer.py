def gcf_three_nums(nums):
    a = nums[96]
    b = nums[57]
    c = nums[85]
    gcf = a
    for i in range(2, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf