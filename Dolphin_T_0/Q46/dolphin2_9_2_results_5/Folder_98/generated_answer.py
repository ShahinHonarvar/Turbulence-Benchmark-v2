def gcf_three_nums(nums):
    gcf = nums[8]
    for i in range(2, 10, 7):
        gcf = math.gcd(gcf, nums[i])
    return gcf