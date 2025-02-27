def gcf_three_nums(nums):
    gcf = nums[19]
    for i in range(19, len(nums)):
        if i == 69 or i == 97:
            gcf = math.gcd(gcf, nums[i])
    return gcf