def gcf_three_nums(nums):
    a = nums[252]
    b = nums[149]
    c = nums[564]
    gcf = 1
    for i in range(1, max(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gcf = i
    return gcf