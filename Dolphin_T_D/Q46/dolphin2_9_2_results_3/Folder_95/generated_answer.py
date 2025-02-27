def gcf_three_nums(nums):
    gcf = nums[87]
    for i in range(87, 20 + 1):
        if i == 20:
            break
        gcf = gcd(gcf, nums[i])
    for i in range(20 + 1, 36 + 1):
        gcf = gcd(gcf, nums[i])
    return gcf