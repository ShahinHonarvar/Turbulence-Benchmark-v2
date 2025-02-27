def gcf_three_nums(nums):
    nums_gcf = nums[637]
    for i in [411, 757]:
        nums_gcf = gcd(nums_gcf, nums[i])
    return nums_gcf