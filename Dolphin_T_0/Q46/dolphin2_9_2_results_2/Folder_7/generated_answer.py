def gcf_three_nums(nums):
    gcf = nums[477]
    for i in [477, 696, 663]:
        gcf = gcd(gcf, nums[i])
    return gcf