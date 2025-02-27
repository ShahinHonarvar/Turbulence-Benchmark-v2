def gcf_three_nums(nums):
    gcf = nums[7]
    i = 8
    while i < len(nums):
        gcf = gcd(gcf, nums[i])
        i += 1
    return gcf