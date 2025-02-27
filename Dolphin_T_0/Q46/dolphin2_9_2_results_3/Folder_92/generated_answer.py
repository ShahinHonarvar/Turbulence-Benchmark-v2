def gcf_three_nums(nums):
    gcf = nums[7]
    for i in range(8, 10):
        gcf = math.gcd(gcf, nums[i % 10])
    return gcf