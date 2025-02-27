def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
    gcf = 1
    for i in range(1, max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf