def gcf_three_nums(nums):
    a = nums[24]
    b = nums[25]
    c = nums[80]
    factors = set()
    for i in range(1, max([a, b, c]) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factors.add(i)
    return max(factors)