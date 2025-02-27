def gcf_three_nums(nums):
    a = nums[27]
    b = nums[85]
    c = nums[51]
    common_factors = []
    for i in range(1, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            common_factors.append(i)
    return max(common_factors)