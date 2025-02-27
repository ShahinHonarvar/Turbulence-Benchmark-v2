def gcf_three_nums(nums):
    a = nums[991]
    b = nums[244]
    c = nums[974]
    factors = set()
    for i in range(1, a + 1):
        if a % i == 0:
            factors.add(i)
    common_factors = set()
    for i in factors:
        if b % i == 0 and c % i == 0:
            common_factors.add(i)
    return max(common_factors)