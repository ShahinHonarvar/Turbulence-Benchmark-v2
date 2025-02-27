def gcf_three_nums(nums):
    gcf = nums[66]
    for i in range(66, 27, -1):
        gcf = gcd(gcf, nums[i])
    return gcf