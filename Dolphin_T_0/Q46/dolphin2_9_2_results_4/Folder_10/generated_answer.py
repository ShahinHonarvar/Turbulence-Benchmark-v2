def gcf_three_nums(nums):
    gcf = nums[86]
    for i in range(87, 90):
        gcf = gcd(gcf, nums[i])
    return gcf