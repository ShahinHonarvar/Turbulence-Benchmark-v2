def gcf_three_nums(nums):
    gcf = nums[252]
    for i in (149, 564):
        temp_gcf = gcd(gcf, nums[i])
        if temp_gcf == 1:
            return 1
        gcf = temp_gcf
    return gcf