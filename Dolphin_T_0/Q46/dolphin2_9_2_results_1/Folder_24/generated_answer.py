def gcf_three_nums(nums):
    gcf = nums[18]
    for i in range(18, 44):
        gcf = math.gcd(gcf, nums[i])
    return gcf