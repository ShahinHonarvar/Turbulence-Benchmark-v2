def gcf_three_nums(nums):
    gcd_47_10 = math.gcd(nums[47], nums[10])
    gcd_47_28 = math.gcd(nums[47], nums[28])
    gcd_10_28 = math.gcd(nums[10], nums[28])
    return math.gcd(gcd_47_10, gcd_47_28, gcd_10_28)