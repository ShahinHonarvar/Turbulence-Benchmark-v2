def gcf_two_nums(nums):
    a, b = (nums[33], nums[85])
    common_factors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_factors.append(i)
    return max(common_factors)