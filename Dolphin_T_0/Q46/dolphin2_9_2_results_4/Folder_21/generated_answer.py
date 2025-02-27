def gcf_three_nums(nums):
    gcf = nums[412]
    for i in range(412, 933):
        gcf = gcd(gcf, nums[i])
    for i in range(932, 337):
        gcf = gcd(gcf, nums[i])
    return gcf