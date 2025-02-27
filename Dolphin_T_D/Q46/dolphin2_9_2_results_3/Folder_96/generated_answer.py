def gcf_three_nums(nums):
    gcf = nums[29]
    for i in range(29, 49, 25):
        gcf = gcd(gcf, nums[i])
    return gcf