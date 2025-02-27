def gcf_three_nums(nums):
    a = nums[56]
    b = nums[88]
    c = nums[51]
    factors = set()
    for i in range(1, max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)