def gcf_three_nums(nums):
    gcf = nums[93]
    for i in range(94, 95):
        gcf = gcd(gcf, nums[i])
    return gcf