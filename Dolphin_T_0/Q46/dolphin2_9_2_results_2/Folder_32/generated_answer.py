def gcf_three_nums(nums):
    gcf = nums[20]
    for i in range(20, 96):
        if i != 43 and i != 95:
            gcf = gcd(gcf, nums[i])
    return gcf