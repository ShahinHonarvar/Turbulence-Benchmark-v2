def gcf_three_nums(nums):
    gcf = nums[31]
    for i in [69, 40]:
        gcf = gcd(gcf, nums[i])
    return gcf