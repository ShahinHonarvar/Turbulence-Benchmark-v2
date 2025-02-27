def gcf_three_nums(nums):
    nums = [nums[8], nums[2], nums[1]]
    gcf = nums[0]
    for i in range(1, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf