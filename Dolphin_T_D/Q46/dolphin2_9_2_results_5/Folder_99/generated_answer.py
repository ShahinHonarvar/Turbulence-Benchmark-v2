def gcf_three_nums(nums):
    gcf = nums[912]
    for i in [170, 500]:
        if gcf > nums[i]:
            gcf = math.gcd(gcf, nums[i])
        else:
            gcf = math.gcd(nums[i], gcf)
    return gcf