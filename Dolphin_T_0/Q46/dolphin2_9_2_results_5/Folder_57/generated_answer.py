def gcf_three_nums(nums):
    a = nums[90]
    b = nums[41]
    c = nums[95]
    factors = set()
    for i in range(min(a, b, c), 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)