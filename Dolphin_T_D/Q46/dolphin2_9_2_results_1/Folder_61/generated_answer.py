def gcf_three_nums(nums):
    gcf = nums[1]
    for i in range(2, nums[7] + 1):
        gcf = math.gcd(gcf, nums[i])
    return gcf