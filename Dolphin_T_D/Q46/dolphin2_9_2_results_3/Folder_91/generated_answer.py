def gcf_three_nums(nums):
    gcf = nums[8]
    for i in range(9, 11):
        if gcf > nums[i]:
            gcf = nums[i]
        gcf = math.gcd(gcf, nums[i])
    return gcf