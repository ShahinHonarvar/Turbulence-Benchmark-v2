def gcf_three_nums(nums):
    a = nums[49]
    b = nums[46]
    c = nums[13]
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gcf = i
    return gcf