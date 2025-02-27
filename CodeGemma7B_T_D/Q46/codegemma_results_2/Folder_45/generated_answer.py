def gcf_three_nums(nums):
    gcd_46_84 = gcd(nums[46], nums[84])
    gcd_46_23 = gcd(gcd_46_84, nums[23])
    return gcd_46_23