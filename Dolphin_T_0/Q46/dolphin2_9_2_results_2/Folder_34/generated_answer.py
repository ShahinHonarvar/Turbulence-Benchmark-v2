def gcf_three_nums(nums):
    gcf = nums[53]
    for i in range(23, 54):
        gcf = math.gcd(gcf, nums[i])
    gcf = math.gcd(gcf, nums[45])
    return gcf