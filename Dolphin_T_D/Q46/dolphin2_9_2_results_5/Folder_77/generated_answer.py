def gcf_three_nums(nums):
    gcf = nums[693]
    for i in range(693, 694):
        gcf = gcd(gcf, nums[i + 1])
    return gcf